from django.db import models

import pathlib
import pickle
import joblib
import json
import numpy as np
from sklearn import preprocessing
import pandas as pd
from django.http import HttpResponse
from underthesea import word_tokenize
import string
import requests
import regex as re
from django.contrib import messages
import tensorflow as tf
from tensorflow import keras
from PIL import Image
pipeline= joblib.load("/app/backend/model/pipeline.pkl")
label = joblib.load("/app/backend/model/label.pkl")
modelll= tf.keras.models.load_model('model_image')
class homepage(models.Model):
	text=models.CharField(max_length=1000)
	text2=models.CharField(max_length=1000)
	url=models.URLField(max_length=1000,null=True)
	class Meta:
		managed = True
	def save(self, *args, **kwargs):
		if self.text2=='Null':
			self.text2=Chat(self.text,False)
		else:
			self.text2=Chat(self.text2,True)
		super(homepage, self).save(*args, **kwargs)

class ImageModel(models.Model):
    image=models.ImageField()
    
    class Meta:
        managed = True

    def save(self, *args, **kwargs):
       
        img=(Image.open(self.image)).resize((180,180))
        img_array = keras.preprocessing.image.img_to_array(img)
        img_array = tf.expand_dims(img_array, 0) 
        predictions = modelll.predict(img_array)
        score = tf.nn.softmax(predictions[0])
        class_names=['Đầm lưới', 'Đầm nude', 'Đầm Nút', 'Đầm vest']
        homepage.objects.create(text='Null',text2=class_names[np.argmax(score)],url="http://127.0.0.1:8000"+self.image.url)
        super(ImageModel, self).save(*args, **kwargs)
        
		
       

class ProductModel(models.Model):
    Name=models.CharField(max_length=1000)
    Size=models.CharField(max_length=1000)
    Color=models.CharField(max_length=1000)
    Number=models.IntegerField(default=100)
    Attribute=models.CharField(max_length=1000)
    class Meta:
        managed = True
class ConversationModel(models.Model):
    NameProduct=models.CharField(max_length=1000)
    Size=models.CharField(max_length=1000,null=True, blank=True)
    Color=models.CharField(max_length=1000,null=True,blank=True)
    Attribute=models.CharField(max_length=1000,null=True,blank=True)
    Name=models.CharField(max_length=1000,null=True,blank=True)
    Height=models.CharField(max_length=1000,null=True,blank=True)
    Width=models.CharField(max_length=1000,null=True,blank=True)
    Number=models.IntegerField(null=True,blank=True)
    Waist=models.CharField(max_length=1000,null=True,blank=True)
    Ass=models.CharField(max_length=1000,null=True,blank=True)
    class Meta:
        managed = True
  

def approvereject(unit):
	try:
		z=unit
		t=[text_preprocess(z)]
		
		t = pipeline.predict(t)
		t= label.inverse_transform(t)
		return  t
	except ValueError as e:
		return Response(e.args[0],	 status.HTTP_400_BAD_REQUEST)
import string

bang_nguyen_am = [['a', 'à', 'á', 'ả', 'ã', 'ạ', 'a'],
				  ['ă', 'ằ', 'ắ', 'ẳ', 'ẵ', 'ặ', 'aw'],
				  ['â', 'ầ', 'ấ', 'ẩ', 'ẫ', 'ậ', 'aa'],
				  ['e', 'è', 'é', 'ẻ', 'ẽ', 'ẹ', 'e'],
				  ['ê', 'ề', 'ế', 'ể', 'ễ', 'ệ', 'ee'],
				  ['i', 'ì', 'í', 'ỉ', 'ĩ', 'ị', 'i'],
				  ['o', 'ò', 'ó', 'ỏ', 'õ', 'ọ', 'o'],
				  ['ô', 'ồ', 'ố', 'ổ', 'ỗ', 'ộ', 'oo'],
				  ['ơ', 'ờ', 'ớ', 'ở', 'ỡ', 'ợ', 'ow'],
				  ['u', 'ù', 'ú', 'ủ', 'ũ', 'ụ', 'u'],
				  ['ư', 'ừ', 'ứ', 'ử', 'ữ', 'ự', 'uw'],
				  ['y', 'ỳ', 'ý', 'ỷ', 'ỹ', 'ỵ', 'y']]
bang_ky_tu_dau = ['', 'f', 's', 'r', 'x', 'j']

nguyen_am_to_ids = {}

for i in range(len(bang_nguyen_am)):
	for j in range(len(bang_nguyen_am[i]) - 1):
		nguyen_am_to_ids[bang_nguyen_am[i][j]] = (i, j)


def chuan_hoa_dau_tu_tieng_viet(word):
	if not is_valid_vietnam_word(word):
		return word

	chars = list(word)
	dau_cau = 0
	nguyen_am_index = []
	qu_or_gi = False
	for index, char in enumerate(chars):
		x, y = nguyen_am_to_ids.get(char, (-1, -1))
		if x == -1:
			continue
		elif x == 9:  # check qu
			if index != 0 and chars[index - 1] == 'q':
				chars[index] = 'u'
				qu_or_gi = True
		elif x == 5:  # check gi
			if index != 0 and chars[index - 1] == 'g':
				chars[index] = 'i'
				qu_or_gi = True
		if y != 0:
			dau_cau = y
			chars[index] = bang_nguyen_am[x][0]
		if not qu_or_gi or index != 1:
			nguyen_am_index.append(index)
	if len(nguyen_am_index) < 2:
		if qu_or_gi:
			if len(chars) == 2:
				x, y = nguyen_am_to_ids.get(chars[1])
				chars[1] = bang_nguyen_am[x][dau_cau]
			else:
				x, y = nguyen_am_to_ids.get(chars[2], (-1, -1))
				if x != -1:
					chars[2] = bang_nguyen_am[x][dau_cau]
				else:
					chars[1] = bang_nguyen_am[5][dau_cau] if chars[1] == 'i' else bang_nguyen_am[9][dau_cau]
			return ''.join(chars)
		return word

	for index in nguyen_am_index:
		x, y = nguyen_am_to_ids[chars[index]]
		if x == 4 or x == 8:  # ê, ơ
			chars[index] = bang_nguyen_am[x][dau_cau]
			# for index2 in nguyen_am_index:
			#     if index2 != index:
			#         x, y = nguyen_am_to_ids[chars[index]]
			#         chars[index2] = bang_nguyen_am[x][0]
			return ''.join(chars)

	if len(nguyen_am_index) == 2:
		if nguyen_am_index[-1] == len(chars) - 1:
			x, y = nguyen_am_to_ids[chars[nguyen_am_index[0]]]
			chars[nguyen_am_index[0]] = bang_nguyen_am[x][dau_cau]
		# x, y = nguyen_am_to_ids[chars[nguyen_am_index[1]]]
		# chars[nguyen_am_index[1]] = bang_nguyen_am[x][0]
		else:
			# x, y = nguyen_am_to_ids[chars[nguyen_am_index[0]]]
			# chars[nguyen_am_index[0]] = bang_nguyen_am[x][0]
			x, y = nguyen_am_to_ids[chars[nguyen_am_index[1]]]
			chars[nguyen_am_index[1]] = bang_nguyen_am[x][dau_cau]
	else:
		# x, y = nguyen_am_to_ids[chars[nguyen_am_index[0]]]
		# chars[nguyen_am_index[0]] = bang_nguyen_am[x][0]
		x, y = nguyen_am_to_ids[chars[nguyen_am_index[1]]]
		chars[nguyen_am_index[1]] = bang_nguyen_am[x][dau_cau]
	# x, y = nguyen_am_to_ids[chars[nguyen_am_index[2]]]
	# chars[nguyen_am_index[2]] = bang_nguyen_am[x][0]
	return ''.join(chars)


def is_valid_vietnam_word(word):
	chars = list(word)
	nguyen_am_index = -1
	for index, char in enumerate(chars):
		x, y = nguyen_am_to_ids.get(char, (-1, -1))
		if x != -1:
			if nguyen_am_index == -1:
				nguyen_am_index = index
			else:
				if index - nguyen_am_index != 1:
					return False
				nguyen_am_index = index
	return True


def chuan_hoa_dau_cau_tieng_viet(sentence):
	"""
        Chuyển câu tiếng việt về chuẩn gõ dấu kiểu cũ.
        :param sentence:
        :return:
        """
	sentence = sentence.lower()
	words = sentence.split()
	for index, word in enumerate(words):
		cw = re.sub(r'(^\p{P}*)([p{L}.]*\p{L}+)(\p{P}*$)', r'\1/\2/\3', word).split('/')
		# print(cw)
		if len(cw) == 3:
			cw[1] = chuan_hoa_dau_tu_tieng_viet(cw[1])
		words[index] = ''.join(cw)
	return ' '.join(words)


# hàm xoá số trong chuỗi
def removeDigits(s):
	result = ''.join([i for i in s if not i.isdigit()])
	return result


# hàm xoá các kí tự đặc biệt và thừa
def removecharacter(s):
	s = s + '.'
	s = s.replace(';', ' ')
	s = s.replace('.', ' ')
	return s


def replacecharacter(s):

	s = ' ' + s
	for i in range(0, 10):
		s = s.replace('xxx', 'xx')
	for i in range(0, 20):
		for t in ['a', 'i', 'o', 'u', 'n', 'e']:
			s = s.replace(t + t, t)
	s = s.replace('j', 'g')
	s = s.replace(' tren ', ' trên ')
	s = s.replace(' nhan ', ' nhận ')
	s = s.replace(' trên lai ', ' trên live ')
	s = s.replace(' xem lai ', ' trên live ')
	s = s.replace(' gi ', ' gì ')
	s = s.replace(' hoan ', ' hoàn ')
	s = s.replace(' dat ', ' đặt ')
	s = s.replace('aon', 'oan')
	s = s.replace('uey', 'uye')
	s = s.replace('euy', 'uye')
	s = s.replace('uyne', 'uyen')
	s = s.replace(' lai ', ' lại ')
	s = s.replace('sz', 'size')
	s = s.replace('sét', ' set ')
	s = s.replace(' noi ', ' nói ')
	s = s.replace(' ns ', ' nói ')
	s = s.replace('lun', 'luôn')
	s = s.replace(' loi ', ' lỗi ')
	s = s.replace(' nham ', ' nhầm ')
	s = s.replace(':', ' : ')
	s = s.replace(' cu ', ' cũ ')
	s = s.replace(' củ ', ' cũ ')
	s = s.replace('dia chi', 'địa chỉ')
	s = s.replace(' chi ', ' chị ')
	s = s.replace(' c ', ' chị ')
	s = s.replace(' b ', ' bạn ')
	s = s.replace(' xã ', ' xả ')
	s = s.replace(' ck ', ' chuyển khoản ')
	s = s.replace(' chuyen khoan ', ' chuyển khoản ')
	s = s.replace(' ban ', ' bạn ')
	s = s.replace(' nge ', ' nghe ')
	s = s.replace(' ha ', ' hả ')
	s = s.replace('uong', 'ương')
	s = s.replace('ug', 'úng')
	s = s.replace('og', 'ong')
	s = s.replace('uon', 'uôn')
	s = s.replace('ien', 'iện')
	s = s.replace(' ãu ', ' ẫu ')
	s = s.replace(' de ', ' để ')
	s = s.replace(' đê ', ' để ')
	s = s.replace(' oi ', ' ạ ')
	s = s.replace(' ơi ', ' ạ ')
	s = s.replace(' ôi ', ' ạ ')
	s = s.replace(' e ', ' em ')
	s = s.replace(' tp ', ' thành phố ')
	s = s.replace(' thanh pho ', ' thành phố ')
	s = s.replace(' phương ', ' phường ')
	s = s.replace(' mau ', ' mẫu ')
	s = s.replace(' set ', ' mẫu ')
	s = s.replace(' diện ', ' điện ')
	s = s.replace(' cai ', ' cái ')
	s = s.replace(' nua ', ' nữa ')
	s = s.replace(' roi ', ' rồi ')
	s = s.replace(' nhe ', ' nha ')
	s = s.replace(' nhen ', ' nha ')
	s = s.replace(' tinh ', ' tỉnh ')
	s = s.replace(' nhé ', ' nha ')
	s = s.replace(' nhá ', ' nha ')
	s = s.replace('đ/c', 'địa chỉ')
	s = s.replace('d/c', 'địa chỉ')
	s = s.replace('sdt', 'số điện thoại')
	s = s.replace(' dt ', ' điện thoại ')
	s = s.replace(' co ', ' có ')
	s = s.replace(' voi ', ' với ')
	s = s.replace(' tren ', ' trên ')
	s = s.replace(' ten ', ' tên ')
	s = s.replace(' ko ', ' không ')
	s = s.replace(' k ', ' không ')
	s = s.replace(' khong ', ' không ')
	s = s.replace(' khog ', ' không ')
	s = s.replace(' doc ', ' đọc ')
	s = s.replace(' dc ', ' được ')
	s = s.replace(' lây ', ' lấy ')
	s = s.replace(' lay ', ' lấy ')
	s = s.replace(' minh ', ' mình ')
	s = s.replace(' k lấy ', ' không lấy ')
	s = s.replace(' chot ', ' chốt ')
	s = s.replace(' lấy ', ' chốt ')
	s = s.replace(' con ', ' còn ')
	s = s.replace(' bo ', ' bộ ')
	s = s.replace('vay để', 'vậy để')
	s = s.replace('vay có', 'vậy có')
	s = s.replace('vay shop', 'vậy shop')
	s = s.replace('không vay', 'không vậy')
	s = s.replace(' vay ', ' váy ')
	s = s.replace(' đương ', ' đường ')
	s = s.replace(' dương ', ' đường ')
	s = s.replace(' gui ', ' gửi ')
	s = s.replace(' goi ', ' gửi ')
	s = s.replace(' so ', ' số ')
	s = s.replace(' gởi ', ' gửi ')
	s = s.replace(' ve ', ' về ')
	s = s.replace(' voi ', ' với ')
	s = s.replace(' vơi ', ' với ')
	s = s.replace(' vs ', ' với ')
	s = s.replace(' vời ', ' với ')
	s = s.replace(' don ', ' đơn ')
	s = s.replace(' vợi ', ' với ')
	s = s.replace(' r ', ' rồi ')
	s = s.replace(' d lại ', ' đổi lại ')
	s = s.replace(' đoi lại', ' đổi lại ')
	s = s.replace(' doi lại ', ' đổi lại ')
	s = s.replace(' khac ', ' khác ')
	s = s.replace(' hang ', ' hàng ')
	s = s.replace('đon hàng', 'đơn hàng')
	s = s.replace('đ hàng', 'đơn hàng')
	s = s.replace('d hàng', 'đơn hàng')
	s = s.replace(' dum ', ' dùm ')
	s = s.replace(' tra hàng ', ' trả về nhầm ')
	s = s.replace(' tra về ', ' trả về nhầm ')
	s = s.replace(' tra lại ', ' trả về nhầm ')
	s = s.replace(' tra cho ', ' trả về nhầm ')
	s = s.replace(' ah ', ' ạ ')
	s = s.replace(' a ', ' ạ ')
	s = s.replace(' chậc ', ' chật ')
	s = s.replace(' hoi chat ', ' hơi chật ')
	s = s.replace(' hoi chật ', ' hơi chật ')
	s = s.replace(' chị ', ' shop ')
	s = s.replace('/', ' / ')
	s = s.replace(' bô ', ' bộ ')
	s = s.replace(' Bô ', ' bộ ')
	s = s.replace(' Đâm ', ' Đầm ')
	s = s.replace(' đầm ', ' Đầm ')
	s = s.replace(' đam ', ' Đầm ')
	s = s.replace(' dam ', ' Đầm ')
	s = s.replace(' mã ', ' Mã ')
	s = s.replace(' set ', ' Set ')
	s = s.replace(' sét ', ' Sét ')
	return s


# hàm tiền xử lí data
def text_preprocess(document):
	# chuẩn hóa cách gõ dấu tiếng Việt
	document = chuan_hoa_dau_cau_tieng_viet(document)
	# đưa về lower
	document = document.lower()
	# remove character
	document = removecharacter(document)
	document = replacecharacter(document)
	# phân loại từ ghép.
	document = word_tokenize(document, format="text")
	# xóa khoảng trắng thừa
	document = re.sub(r'\s+', ' ', document).strip()
	return document







def predictEntity(text):
	text2=text.split()
	t1=['đầm','áo','quần','váy','set','mẫu','Mẫu','Set','Bộ','bộ','mã','Mã','Váy','Áo','Quần','Đầm','vest','Vest','Vét','vet','Vest','body','Sét','sét']
	t2=requests.get('http://127.0.0.1:8000/api/Product/').json()
	t3=[0]*len(t2)
	t4=[]
	for i in range(len(t2)):
  		t4.append(t2[i]['Name'].split())
	max=-1
	z=0
	for item in t1:
		if item in text:
			for i in range(len(t2)):
				for  item2 in t4[i]:
					if item2 in text2:
						t3[i]=t3[i]+1
			for u in range(len(t3)):
				if t3[u]>max:
					max=t3[u]
					z=u
	return t2[z]

def predict(text):
	t=predictEntity(text)
	if t['Number']>0: 
		u='Dạ mẫu '+t['Name']+' này bên em còn các size là: '+t['Size']+' Còn các loại màu: '+t['Color']+' Giá là 10000k'+' Chị cho em xin thông tin chiều cao cân nặng để tư vấn cần tư size ạ'
		ConversationModel.objects.create(Number=1,NameProduct=t['Name'],Attribute=t['Attribute'],Size='Null',Color='Null',Name='Null',Height='Null',Width='Null',Ass='Null',Waist='Null')
	else:
		u='Dạ mẫu này bên em hết hàng rồi ạ, chị có thể vui lòng chọn mẫu khác được không ạ'
	return u

def Chat(text,ok):
	t=approvereject(text)
	z=False
	u='NuLL'

	for i in ['S','s','L','l','m','M']:
		for item in text.split():
			if item==i:
				u=i
				z=True
	if t=='Hello':
		return 'Dạ shop chào chị ạ chị muốn tư vấn sản phẩm nào ạ'
	elif t=='Inform':
		if 'mông' in text.split():
			return HandelAss(text)
		if 'eo' in text.split():
			return HandelWaist(text)
		if 'cao' in text.split():
			pattern ='^1m[0-9]*'
			for item in text.split():
				if re.match(pattern, item):
					UpdateNumber()
					UpdateHeight(item)
					break
		if 'nặng' in text.split():
			pattern1 ='[0-9]*kg$'
			pattern2 ='[0-9]* kg'
			pattern3 ='[0-9]* kí'
			v=''
			t1=re.search(pattern1, text)
			if t1:
				v=t1.group()
			t2=re.search(pattern2,text)
			if t2:
				v=t2.group()
			t3=re.search(pattern3, text)
			if t3:
				v=t3.group()
			if v!='':
				UpdateNumber()
				UpdateWidth(v)
		if GetLastHeight()=='Null' and GetLastWidth()=="Null":
			return "Chị cho em xin chiều cao và cân nặng ạ"
		if GetLastHeight()=='Null':
			return "Chị cho em xin chiều cao ạ"
		if GetLastWidth()=="Null":
			return "Chị cho em xin cân nặng ạ"
		return findSize(text)
	elif  z and t=='Order':
		UpdateSize(u)
		return "Dạ chị chọn size "+ u + " ạ."	

	else:

		if ok:
			return predict(text)
		if GetLastNumber()<3:
			if GetLastHeight()=='Null':
				return "Chị cho em xin chiều cao ạ"
			if GetLastWidth()=="Null":
				return "Chị cho em xin cân nặng ạ"
		if 'k' in text.split() or 'không' in text.split() or 'ko' in text.split():
			if GetLastNumber()==3:
				UpdateNumber()
				return "Vậy Chị cho em hỏi số đo mông ạ"
			if GetLastNumber()==4:
				UpdateNumber()
				return CusSize()
		return 'Dạ xin lỗi em chưa hiểu ý chị ạ'


def UpdateSize(text):
	t2=requests.get('http://127.0.0.1:8000/api/Conversation/').json()
	name=t2[len(t2)-1]['Name']
	ConversationModel.objects.filter(Name=name).update(Size=text)
def UpdateHeight(text):
	t2=requests.get('http://127.0.0.1:8000/api/Conversation/').json()
	name=t2[len(t2)-1]['Name']
	ConversationModel.objects.filter(Name=name).update(Height=text)

def UpdateWidth(text):
	t2=requests.get('http://127.0.0.1:8000/api/Conversation/').json()
	name=t2[len(t2)-1]['Name']
	ConversationModel.objects.filter(Name=name).update(Width=text)

def UpdateAss(text):
	t2=requests.get('http://127.0.0.1:8000/api/Conversation/').json()
	name=t2[len(t2)-1]['Name']
	ConversationModel.objects.filter(Name=name).update(Ass=text)

def UpdateWaist(text):
	t2=requests.get('http://127.0.0.1:8000/api/Conversation/').json()
	name=t2[len(t2)-1]['Name']
	ConversationModel.objects.filter(Name=name).update(Waist=text)

def UpdateNumber():
	t2=requests.get('http://127.0.0.1:8000/api/Conversation/').json()
	name=t2[len(t2)-1]['Name']
	ConversationModel.objects.filter(Name=name).update(Number=Number+1)

def GetLastSize():
	t2=requests.get('http://127.0.0.1:8000/api/Conversation/').json()
	return t2[len(t2)-1]['Size']
	

def GetLastHeight():
	t2=requests.get('http://127.0.0.1:8000/api/Conversation/').json()
	return t2[len(t2)-1]['Height']
	

def GetLastWidth():
	t2=requests.get('http://127.0.0.1:8000/api/Conversation/').json()
	return t2[len(t2)-1]['Width']
def GetLastWaist():
	t2=requests.get('http://127.0.0.1:8000/api/Conversation/').json()
	return t2[len(t2)-1]['Waist']
def GetLastAss():
	t2=requests.get('http://127.0.0.1:8000/api/Conversation/').json()
	return t2[len(t2)-1]['Ass']
def GetLastNumber():
	t2=requests.get('http://127.0.0.1:8000/api/Conversation/').json()
	return t2[len(t2)-1]['Number']	


def findSize(text):
	UpdateNumber()
	return "Chị cho em hỏi số đo eo ạ"

def HandelWaist(text):

	pattern1 ='[0-9]*cm$'
	pattern2 ='[0-9]* cm'
	pattern3 ='[0-9]* cen'
	v=''
	t1=re.search(pattern1, text)
	if t1:
		v=t1.group()
	t2=re.search(pattern2,text)
	if t2:
		v=t2.group()
	t3=re.search(pattern3, text)
	if t3:
		v=t3.group()
	if v!='':
		UpdateWaist(v)
		UpdateNumber()
	return "Chị cho em hỏi số đo mông ạ"
def HandelAss(text):
	pattern1 ='[0-9]*cm$'
	pattern2 ='[0-9]* cm'
	pattern3 ='[0-9]* cen'
	v=''
	t1=re.search(pattern1, text)
	if t1:
		v=t1.group()
	t2=re.search(pattern2,text)
	if t2:
		v=t2.group()
	t3=re.search(pattern3, text)
	if t3:
		v=t3.group()
	if v!='':
		UpdateAss(v)
		UpdateNumber()
	return CusSize()
def CusSize():
	return "size của chị là size S ạ"
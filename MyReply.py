#-*-coding:utf-8 -*-
def reply(origin):
	origin = origin.decode('utf-8')
	if fucking_words(origin):
		return origin
	return u"你好，我是friparia的助理，有事请留言"

def fucking_words(coming_words):
	fucking_words = ['sb', u'炸了', u'蠢', 'fuck', u'你妈', u'尼玛', u'bitch', '碧池']
	for word in fucking_words:
		if coming_words.find(word) != -1:
			return True
	return False

while True:
	input = raw_input("Say Something:")
	if input == 'exit':
		break
	print reply(input)

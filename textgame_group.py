import pygame
import time
import pickle

pygame.init()

pygame.font.get_fonts()

red = (255,0,0)
white = (255,255,255)
black = (0,0,0)
bright_black = (50, 50, 50)
bright_gray = (209, 209, 209)
dark_gray = (143,143,143)

screen_width = 1280
screen_height = 720

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('testing game')
pygame.display.update()

clock = pygame.time.Clock()

#crowdtalk_sound = pygame.mixer.Sound('talk_cut.wav')


font = pygame.font.SysFont('mingliupmingliumingliuhkscs',20)
font_for_title = pygame.font.SysFont('mingliupmingliumingliuhkscs',25)
#font_for_opening = pygame.font.SysFont('mingliupmingliumingliuhkscs',25)

theblock_for_changing_background = 6
	
def message_to_screen(msg,color,x,y):
	screen_text = font.render(msg,True,color)
	screen.blit(screen_text,[x,y])
	
	
def message_to_screen_for_title(msg,color,x,y):
	screen_text = font_for_title.render(msg,True,color)
	screen.blit(screen_text,[x,y])
	
def show_text_name_for_2(textforname):
	message_to_screen_for_title(textforname,black,130,480)
	pygame.display.update()
	
def show_text_name_for_4(textforname):
	#姓和名中間要加3個block
	message_to_screen_for_title(textforname,black,80,480)
	pygame.display.update()
	
def show_text_1(text1):
	message_to_screen(text1,black,55,580)
	pygame.display.update()
	
def show_text_2(text2):
	message_to_screen(text2,black,55,612)
	pygame.display.update()
	
def show_text_3(text3):
	message_to_screen(text3,black,55,644)
	pygame.display.update()
	
def show_text_4(text4):
	message_to_screen(text4,black,55,676)
	pygame.display.update()
	
def original_board(bg):
	global background_file, background
	background_file = bg
	background = pygame.image.load(background_file).convert()
	screen.blit(background, (0, 0))
	pygame.display.update()
	
class two_background(pygame.sprite.Sprite):
	
	def __init__(self, screen, nowback, newback):
		pygame.sprite.Sprite.__init__(self)
		
		self.pre_background = nowback
		self.des_background = newback
		
		self.preback = pygame.image.load(self.pre_background)
		self.preback = self.preback.convert()
		self.desback = pygame.image.load(self.des_background)
		self.desback = self.desback.convert()
		
		self.images = [self.preback, self.desback]
		self.image = self.images[0]
		self.rect = self.image.get_rect()
		self.screen = screen
		
		self.i = 0
		
	def update(self):
		self.rect.centerx = (screen_width / 2)
		self.rect.centery = (screen_height / 2)
		self.image = self.images[self.i]

		
		

class CrossFade(pygame.sprite.Sprite):
	
	def __init__(self, screen):
		pygame.sprite.Sprite.__init__(self)
		
		self.image = pygame.Surface(screen.get_size())
		self.image = self.image.convert()
		#self.image.fill((0, 0, 0))
		
		self.rect = self.image.get_rect()
		
		self.fade_dir = 1
		
		self.trans_value = 0
		
		self.fade_speed = 6
		
		self.delay = 1
		
		self.image.set_alpha(self.trans_value)
		
		self.rect.centerx = screen_width / 2
		self.rect.centery = screen_height / 2
		
	def update(self):
		self.image.set_alpha(self.trans_value)	
		
		if self.fade_dir > 0:
				
			if self.trans_value - self.fade_speed < 0:
				self.trans_value = 0
			else:
				self.trans_value -= self.fade_speed
					
					
		elif self.fade_dir < 0:
				
			if self.trans_value + self.delay > 225:
				self.trans_value = 225
			else:
				self.trans_value += self.fade_speed


def change_background(now, new, changespeed):
	global screen, background
	
	fade = CrossFade(screen)

	back_surface = two_background(screen,now, new)
	
	all_Sprites = pygame.sprite.OrderedUpdates(back_surface, fade)
	
	havebeenfaded = False
	havebeenchanged = False
	
	
			
			
	while not havebeenchanged:
		clock.tick(60)
		pygame.time.delay(changespeed)
		
		if fade.trans_value == 0:
			fade.fade_dir *= -1
			
		all_Sprites.clear(screen, background)
		all_Sprites.update()
		all_Sprites.draw(screen)
		if fade.trans_value == 225:
			back_surface.i = 1
			fade.fade_dir = 1
			all_Sprites.clear(screen, background)
			all_Sprites.update()
			all_Sprites.draw(screen)
			havebeenfaded = True
		if fade.trans_value == 0 and havebeenfaded == True:
			havebeenchanged = True
			#return theblock_for_changing_background
			
		pygame.display.flip()



def saving():
	global x, par, chapter_pointer, musicfrom, goch1, goch2, goch3, data, background_file, gameExit, nowplaying, playmusic, playmusic2
	
	saved = False
	while not saved:
		pygame.draw.rect(screen, black, [200, 50, 700, 70])
		message_to_screen("WHICH FILE DO YOU WANT TO SAVE THE GAME?(1/2/3)", white, 210, 70)
		pygame.display.flip()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					saved = True
				if event.key == pygame.K_1:
					musicfrom += float(pygame.mixer.music.get_pos() / 1000)
					data = [x, par, chapter_pointer, musicfrom, goch1, goch2, goch3, background_file, nowplaying, playmusic, playmusic2]
					with open("saved1", "wb") as f:
						pickle.dump(data, f)
						f.close()
						saved = True
				if event.key == pygame.K_2:
					musicfrom += float(pygame.mixer.music.get_pos() / 1000)
					data = [x, par, chapter_pointer, musicfrom, goch1, goch2, goch3, background_file, nowplaying, playmusic, playmusic2]
					with open("saved2", "wb") as f:
						pickle.dump(data, f)
						f.close()
						saved = True
				if event.key == pygame.K_3:
					musicfrom += float(pygame.mixer.music.get_pos() / 1000)
					data = [x, par, chapter_pointer, musicfrom, goch1, goch2, goch3, background_file, nowplaying, playmusic, playmusic2]
					with open("saved3", "wb") as f:
						pickle.dump(data, f)
						f.close()
						saved = True
	
	gameExit = True			
	
	
def loading():
	global x, par, chapter_pointer, musicfrom, goch1, goch2, goch3, data, background_file, gameExit, nowplaying, playmusic, playmusic2, loaded
	
	original_board(background_file)
	
	loaded = False	
	while not loaded:
		#global x, par, chapter_pointer, musicfrom, goch1, goch2, goch3, data, background_file
		
		#clock.tick(60)

		
		#pygame.draw.rect(screen, black, [540, 400, 200, 50], 5)
		message_to_screen_for_title("NEW GAME",black,590,412.5)
		
		#pygame.draw.rect(screen, black, [540, 480, 200, 50], 5)
		message_to_screen_for_title("DATA1",black,610,492.5)
		
		#pygame.draw.rect(screen, black, [540, 560, 200, 50], 5)
		message_to_screen_for_title("DATA2",black,610,572.5)
		
		#pygame.draw.rect(screen, black, [540, 640, 200, 50], 5)
		message_to_screen_for_title("DATA3",black,610,652.5)
		#pygame.display.flip()	
		
		if loaded == False:
			button_for_intro(540, 400, 200, 50, 5, bright_gray, dark_gray, "NEW GAME")
		if loaded == False:
			button_for_intro(540, 480, 200, 50, 5, bright_gray, dark_gray, "DATA1")
		if loaded == False:
			button_for_intro(540, 560, 200, 50, 5, bright_gray, dark_gray, "DATA2")
		if loaded == False:
			button_for_intro(540, 640, 200, 50, 5, bright_gray, dark_gray, "DATA3")
		
		
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_n:	
					loaded = True
					change_background("start.png", "blackopening.png", 20)
					background_file = "blackopening.png"
				
				if event.key == pygame.K_1:	
					with open("saved1", "rb") as f:
						data = pickle.load(f)						
					x = data[0]
					par = data[1]
					chapter_pointer = data[2]
					musicfrom = data[3]
					goch1 = data[4]
					goch2 = data[5]
					goch3 = data[6]
					background_file = data[7]
					nowplaying = data[8]
					playmusic = data[9]
					playmusic2 = data[10]
					loaded = True
					change_background("start.png", background_file, 20)
					
				if event.key == pygame.K_2:
					with open("saved2", "rb") as f:
						data = pickle.load(f)							
					x = data[0]
					par = data[1]
					chapter_pointer = data[2]
					musicfrom = data[3]
					goch1 = data[4]
					goch2 = data[5]
					goch3 = data[6]
					background_file = data[7]
					nowplaying = data[8]
					playmusic = data[9]
					playmusic2 = data[10]
					loaded = True
					change_background("start.png", background_file, 20)
					
				if event.key == pygame.K_3:
					with open("saved3", "rb") as f:
						data = pickle.load(f)									
					x = data[0]
					par = data[1]
					chapter_pointer = data[2]
					musicfrom = data[3]
					goch1 = data[4]
					goch2 = data[5]
					goch3 = data[6]
					background_file = data[7]
					nowplaying = data[8]
					playmusic = data[9]
					playmusic2 = data[10]
					loaded = True
					change_background("start.png", background_file, 20)
			

def button_for_intro(x_pos, y, w, h, line_thickness, ic, ac, whattodo = None):
	global x, par, chapter_pointer, musicfrom, goch1, goch2, goch3, data, background_file, gameExit, nowplaying, playmusic, playmusic2, loaded
	
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	
	if x_pos < mouse[0] < x_pos + w and y < mouse[1] < y + h:
		pygame.draw.rect(screen, ac, [x_pos, y, w, h], line_thickness)
		if click[0] == 1 and whattodo != None:
			if whattodo == "NEW GAME":
				loaded = True
				change_background("start.png", "blackopening.png", 20)
				background_file = "blackopening.png"
			elif whattodo == "DATA1":
				with open("saved1", "rb") as f:
						data = pickle.load(f)						
				x = data[0]
				par = data[1]
				chapter_pointer = data[2]
				musicfrom = data[3]
				goch1 = data[4]
				goch2 = data[5]
				goch3 = data[6]
				background_file = data[7]
				nowplaying = data[8]
				playmusic = data[9]
				playmusic2 = data[10]
				loaded = True
				change_background("start.png", background_file, 20)
			elif whattodo == "DATA2":
				with open("saved2", "rb") as f:
						data = pickle.load(f)							
				x = data[0]
				par = data[1]
				chapter_pointer = data[2]
				musicfrom = data[3]
				goch1 = data[4]
				goch2 = data[5]
				goch3 = data[6]
				background_file = data[7]
				nowplaying = data[8]
				playmusic = data[9]
				playmusic2 = data[10]
				loaded = True
				change_background("start.png", background_file, 20)
			elif whattodo == "DATA3":
				with open("saved3", "rb") as f:
						data = pickle.load(f)									
				x = data[0]
				par = data[1]
				chapter_pointer = data[2]
				musicfrom = data[3]
				goch1 = data[4]
				goch2 = data[5]
				goch3 = data[6]
				background_file = data[7]
				nowplaying = data[8]
				playmusic = data[9]
				playmusic2 = data[10]
				loaded = True
				change_background("start.png", background_file, 20)
				
	else:
		pygame.draw.rect(screen, ic, [x_pos, y, w, h], line_thickness)
		
	
	pygame.display.flip()	



def button_for_chapter(msg, x_pos, y, w, h, line_thickness, ic, ac, whattodo = None):
	global x, par, chapter_pointer, musicfrom, goch1, goch2, goch3, data, background_file, gameExit, nowplaying, playmusic, playmusic2, loaded, choice, z
	
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	
	message_to_screen(msg, black, x_pos + 20, y + 5)
	
	if x_pos < mouse[0] < x_pos + w and y < mouse[1] < y + h:
		pygame.draw.rect(screen, ac, [x_pos, y, w, h], line_thickness)
		if click[0] == 1 and whattodo != None:
			if whattodo == "兩位關係真不錯，我在這都沒認識的人哈哈":
				choice = 1
				z = 1
			elif whattodo == "真假，為什麼不用客氣啊，客氣不好嗎==":
				choice = 2
				z = 1
			elif whattodo == "那他講幹話的時候我嗆爆妳可以嗎":
				choice = 3
				z = 1
			
			elif whattodo == "剛好沒甚麼事，就出去逛逛吧":
				choice = 1
				z = 1
			elif whattodo == "在宿舍讀書好了":
				choice = 2
				z = 1
				
	else:
		pygame.draw.rect(screen, ic, [x_pos, y, w, h], line_thickness)
		
	
	pygame.display.flip()	
	
	
	
def chapter_1():
	global x, goch1, par, theblock_for_changing_background, playmusic, playmusic2, nowplaying, musicfrom, choice, z
	
	
	
	if par == 1:
		theblock_for_changing_background = 12 + 1
		
		if playmusic == True:
			pygame.mixer.music.fadeout(1000)
			pygame.mixer.music.load("cr_music.mp3")
			musicfrom = 0
			nowplaying = "cr_music.mp3"
			pygame.mixer.music.play(-1)	
			playmusic = False
			
		if x == 0:
			original_board("黒+對話框.png")
		elif x == 1:
			show_text_1("曾幾何時，我們睜開眼不再做夢，夢只能隱晦的收藏？")
		elif x == 2:
			show_text_2("曾幾何時，空白筆記填滿的是數學公式，而非一條蛇吞了大象？")
		elif x == 3:
			show_text_3("我不是我，我是一張張成績單。專心讀書，進好大學出社會，當個成功的人，幸福就會不請自來。")
		elif x == 4:
			show_text_4("大人是這樣說的，所以我這樣做。")
		elif x == 5:
			original_board("黒+對話框.png")
			x += 1
		elif x == 6:
			show_text_1("我們都被豢養，所以不需要飛翔。")
		elif x == 7:
			show_text_2("18歲了，如果考得不好，我應該負責嗎？")
		elif x == 8:
			show_text_3("進大學了，我需要負責嗎？")
		elif x == 9:
			show_text_4("這是我的選擇嗎？")
		elif x == 10:
			original_board("黒+對話框.png")
		elif x == 11:
			show_text_1("說得好像我有得選一樣。")
		elif x == 12:
			change_background("黒+對話框.png", "校園+對話框.png", 30)
			par += 1
			x = 0
	
	
	

	elif par == 2:
		theblock_for_changing_background = 20 + 1
		
		if playmusic2 == True:
			pygame.mixer.music.fadeout(1000)
			pygame.mixer.music.load("kara_m01.mp3")
			musicfrom = 0
			nowplaying = "kara_m01.mp3"
			pygame.mixer.music.play(-1)	
			playmusic2 = False
			
			
		if x == 0:
			original_board("校園+對話框.png")
		elif x == 1:
			show_text_1("開學典禮")
		elif x == 2:
			original_board("校園+對話框+名字框.png")
			#pygame.mixer.Sound.play(crowdtalk_sound)
		elif x == 3:
			show_text_name_for_2("校長")
		elif x == 4:
			show_text_1("歡迎來到伯勞大學！")
		elif x == 5:
			show_text_2("在這令人興奮的時刻，我在台上看到的是一朵朵生機盎然的嫩芽，渴望著養分灌溉。")
		elif x == 6:
			show_text_3("本校是何其榮幸，能做為孕育優秀如你們的搖籃。")
		elif x == 7:
			show_text_4("從收到入學通知書的那一刻起，你們就代表了本校，和本校的未來。")
		elif x == 8:
			original_board("校園+對話框+名字框.png")
			x += 1
		elif x == 9:
			show_text_name_for_2("校長")
			show_text_1("今日你以__大為榮，他日__大將以你為榮，恭喜各位！")
		elif x == 10:
			original_board("校園+對話框+名字框.png")
			x += 1
		elif x == 11:
			show_text_name_for_2("校長")
		elif x == 12:
			show_text_1("我們來自不同的地方，有著不同的背景，一個人的際遇造就了現在的自己，而我們現在齊聚在這裡。")
		elif x == 13:
			show_text_2("你們想成為怎麼樣的人呢？我期待你們能在這階段結交好友，成就自己。")
		elif x == 14:
			show_text_3("你也許會困惑，你一定會遇到困難，但請記得你並不是一個人。")
		elif x == 15:
			original_board("校園+對話框+名字框.png")
			x += 1
		elif x == 16:
			show_text_name_for_2("校長")
		elif x == 17:
			show_text_1("大學是各位一生至關重要的階段，一個人的選擇，編織了一段段不同的人生，串聯起一篇篇精彩的故事。")
		elif x == 18:
			show_text_2("請尊重引導你們的師長，謹言慎行、服從校規。")
		elif x == 19:
			show_text_3("當你們面臨進行重大抉擇的時刻，請務必慎重，並為自己的選擇負起責任。")
		elif x == 20:
			original_board("校園+對話框.png")
			par += 1
			x = 0
			
	elif par == 3:
		theblock_for_changing_background = 5 + 1
		if x == 0:
			original_board("校園+對話框.png")
		elif x == 1:
			show_text_1("所有校長都有的共通點，廢話特多，而且都是老爺爺。校長上台開講已經有20分鐘，感覺還要一陣子。")
		elif x == 2:
			show_text_2("大部分的學生都已經沒有耐心聽演講，有些開始滑手機，有些開始和身邊的人搭訕自我介紹。")
		elif x == 3:
			show_text_3("入學第一天除了參加入學典禮也沒有其他事情會發生。我百無聊賴地拿出手機滑了起來。")
		elif x == 4:
			show_text_4("(開學典禮結束)")
		elif x == 5:
			change_background("校園+對話框.png", "教室+對話框.png", 30)
			par += 1
			x = 0
			
			
			
	elif par == 4:
		theblock_for_changing_background = 7 + 1
		if x == 0:
			original_board("教室+對話框.png")
		elif x == 1:
			show_text_1("（第一堂課）")
		elif x == 2:
			original_board("教室+對話框.png")
		elif x == 3:
			show_text_1("第一堂課，周圍坐的系上同學大約也有上百位...我們真算是一個大系，想到要記起這上百人的名字，就覺得寧願去背英文單字。。")
		elif x == 4:
			show_text_2("教室是個階梯式講堂，高中時也只有在大一點的特殊教室或補習班才看的到這種形式。")
		elif x == 5:
			show_text_3("雖然人數眾多，教室內的氣氛大致是低迷的，只有少數互相認識的人低聲交談。")
		elif x == 6:
			show_text_4("這時多少會覺得要是身旁有個認識的人就好了…我亂講的，被認出來多尷尬==")
		elif x == 7:
			change_background("教室+對話框.png", "教室+對話框+名字框.png", 30)
			par += 1
			x = 0
			
			
	elif par == 5:
		theblock_for_changing_background = 10 + 1
		if x == 0:
			original_board("教室+對話框+名字框.png")
		elif x == 1:
			show_text_name_for_2("教授")
			show_text_1("同學們請安靜坐好，開始上課囉")
		elif x == 2:
			original_board("教室+對話框.png")
		elif x == 3:
			show_text_1("拈著陰柔的聲線，看起來年約五六十的教授走進教室，身材有些臃腫。")
		elif x == 4:
			show_text_2("偏圓的臉，黝黑的肌膚和所剩不多的白髮訴說著歲月，但並不影響他的意氣風發。")
		elif x == 5:
			original_board("教室+對話框+名字框.png")
			x += 1
		elif x == 6:
			show_text_name_for_2("教授")
		elif x == 7:
			show_text_1("還是不免俗地說一句歡迎各位來到伯勞大學。在剛脫離升學壓力，迎接新生活的階段，我明白大家都還是很亢奮的。")
		elif x == 8:
			show_text_2("但也要勸各位盡早收起浮躁，好好努力才是真的。")
		elif x == 9:
			show_text_3("教授在大學時代，大家都在辦活動在玩的時候，我總是一個人在圖書館．．．．．．")
		elif x == 10:
			original_board("教室+對話框.png")
			par += 1
			x = 0
			
			
	elif par == 6:
		theblock_for_changing_background = 8 + 1
		if x == 0:
			original_board("教室+對話框.png")
		elif x == 1:
			show_text_1("教授開始說起當年他是如何寒窗十年無人問、取得今日規模的成就、羨煞多少浮世眾生．．．．．．")
		elif x == 2:
			show_text_2("又扯一些什麼沒實力就等淘汰啊、什麼人脈很重要啊、眼光放遠才能獲得最大利益等等等等。")
		elif x == 3:
			original_board("教室+對話框.png")
			x += 1
		elif x == 4:
			show_text_1("天啊，管院的人都這樣嗎？")
		elif x == 5:
			show_text_2("我以後會變得和他一樣嗎？")
		elif x == 6:
			show_text_3("不好吧==")
		elif x == 7:
			show_text_4("現在回頭太遲了嗎？")
		elif x == 8:
			original_board("教室+對話框+名字框.png")
			par += 1
			x = 0
			
	elif par == 7:
		theblock_for_changing_background = 4 + 1
		if x == 0:
			original_board("教室+對話框+名字框.png")
			x += 1
		elif x == 1:
			show_text_name_for_2("教授")
		elif x == 2:
			show_text_1("．．．．．．以後進了職場，一個重要的能力就是和人群說話，那就是我們今天要做的事啦。")
		elif x == 3:
			show_text_2("請大家上台用一分鐘介紹你自己，下次再開始上正課。")
		elif x == 4:
			original_board("教室+對話框.png")
			par += 1
			x = 0
			
	elif par == 8:
		theblock_for_changing_background = 5 + 1
		if x == 0:
			original_board("教室+對話框.png")
			x += 1
		elif x == 1:
			show_text_1("教授拿出事先護貝好的名牌，讓大家能看清楚接下來上台的人的名字。")
		elif x == 2:
			show_text_2("第一堂課就是上百人一個一個自我介紹，")
		elif x == 3:
			show_text_3("這種方式雖然對認識人沒什麼幫助，但似乎也沒有更好的方法了。")
		elif x == 4:
			show_text_4("一開始大家都還試著掰出一分鐘的長度，後來漸漸地大家就開始無視這規則了......而我也是這麼打算的。")
		elif x == 5:
			change_background("教室+對話框.png", "教室+對話框+名字框.png", 10)
			par += 1
			x = 0
	
	
	elif par == 9:
		theblock_for_changing_background = 6 + 1
		if x == 0:
			original_board("教室+對話框+名字框.png")
		elif x == 1:
			show_text_name_for_4("御影   翔平")
			show_text_1("我叫御影翔平，希望能和大家好好相處，請多指教。")
		elif x == 2:
			original_board("教室+對話框.png")
		elif x == 3:
			show_text_1("台下響起些微意思性的掌聲送我回到座位，")
		elif x == 4:
			show_text_2("正當我想繼續滑手機時，")
		elif x == 5:
			show_text_3("後方傳來一句男聲。")
		elif x == 6:
			change_background("教室+對話框.png", "教室+好朋友+對話框+名字框.png", 30)
			par += 1
			x = 0
	
	elif par == 10:
		theblock_for_changing_background = 8 + 1
		if x == 0:
			original_board("教室+好朋友+對話框+名字框.png")
		elif x == 1:
			show_text_name_for_2("??")
			show_text_1("這堂課還真奇怪，對吧？")
		elif x == 2:
			original_board("教室+好朋友+對話框.png")
		elif x == 3:
			show_text_1("回頭一看，一個帶著粗框眼鏡的帥氣男孩笑咪咪地看著我。")
		elif x == 4:
			original_board("教室+好朋友+對話框+名字框.png")
		elif x == 5:
			show_text_name_for_2("??")
			show_text_1("我叫神谷智則，御影同學，請多指教。")
		elif x == 6:
			original_board("教室+好朋友+對話框+名字框.png")
		elif x == 7:
			show_text_name_for_4("御影   翔平")
			show_text_1("喔喔嗨，很高興認識你。")
		elif x == 8:
			change_background("教室+好朋友+對話框+名字框.png", "教室+對話框.png", 30)
			par += 1
			x = 0
			
			
	elif par == 11:
		theblock_for_changing_background = 3 + 1
		if x == 0:
			original_board("教室+對話框.png")
		elif x == 1:
			show_text_1("智則他看起來就是那種幽默開朗，大家看到都會喜歡的那種人。")
		elif x == 2:
			show_text_2("可能只是想找個人聊天吧...")
		elif x == 3:
			change_background("教室+對話框.png", "教室+好朋友+對話框+名字框.png", 30)
			par += 1
			x = 0
			
			
			
	elif par == 12:
		theblock_for_changing_background = 21 + 1
		if x == 0:
			original_board("教室+好朋友+對話框+名字框.png")
		elif x == 1:
			show_text_name_for_4("神谷   智則")
			show_text_1("聽我學長說，這教授是我們的鎮系之寶，他有一大堆傳奇故事，讓同學們一屆一屆的傳頌下去。")
		elif x == 2:
			original_board("教室+好朋友+對話框+名字框.png")
		elif x == 3:
			show_text_name_for_4("御影   翔平")
			show_text_1("是喔，像是什麼？")
		elif x == 4:
			original_board("教室+好朋友+對話框+名字框.png")
		elif x == 5:
			show_text_name_for_4("神谷   智則")
			show_text_1("像是人人看到他都得堆滿笑臉的和他打招呼，從前不和他講話的系花看到他就會給個大大的擁抱之類的。")
		elif x == 6:
			original_board("教室+好朋友+對話框+名字框.png")
		elif x == 7:
			show_text_name_for_4("御影   翔平")
			show_text_1("太有錢了吧==，有地位就是任性耶，是不是該出門找工作了啊？")
		elif x == 8:
			original_board("教室+好朋友+對話框+名字框.png")
		elif x == 9:
			show_text_name_for_4("神谷   智則")
			show_text_1("他每屆會選某些「可愛」的學生給予特別的「照顧」，")
		elif x == 10:
			show_text_2("聽說他還單獨請學姐吃過冰淇淋呢，那可是人人稱羨的待遇喔！")
		elif x == 11:
			original_board("教室+好朋友+對話框+名字框.png")
		elif x == 12:
			show_text_name_for_4("御影   翔平")
			show_text_1("天啊好羨慕喔，那教授會不會傳裸照啊？好想看喔==")
		elif x == 13:
			original_board("教室+好朋友+對話框+名字框.png")
		elif x == 14:
			show_text_name_for_4("神谷   智則")
			show_text_1("什麼鬼哈哈哈，")
		elif x == 15:
			show_text_2("，聽說這學校畢業生的就業率是完美的100%，而且他們全都進入了很不錯的大公司呢")
		elif x == 16:
			original_board("教室+好朋友+對話框+名字框.png")
		elif x == 17:
			show_text_name_for_4("御影   翔平")
			show_text_1("這樣啊，我想大家都是一樣看上這點拼命考進來的吧。")
		elif x == 18:
			original_board("教室+好朋友+對話框+名字框.png")
		elif x == 19:
			show_text_name_for_4("神谷   智則")
			show_text_1("對阿，大家都希望能順利畢業並成功就業。")
		elif x == 20:
			show_text_2("對了你看，現在在台上的是我朋友。")
		elif x == 21:
			change_background("教室+好朋友+對話框+名字框.png", "教室+女主+對話框.png", 30)
			par += 1
			x = 0
			
			
	elif par == 13:
		theblock_for_changing_background = 4 + 1
		if x == 0:
			original_board("教室+女主+對話框.png")
		elif x == 1:
			show_text_1("現在在台上的女生，名字叫榊原凜。")
		elif x == 2:
			show_text_2("說話有點小聲，卻是堅定的那種，給人一種無法忽視的感覺。")
		elif x == 3:
			show_text_3("介紹完後，她朝我們這邊走過來。")
		elif x == 4:
			change_background("教室+女主+對話框.png", "教室+好朋友和女主+對話框+名字框.png", 30)
			par += 1
			x = 0
			
	elif par == 14:		
		theblock_for_changing_background = 14 + 1
		if x == 0:
			original_board("教室+好朋友和女主+對話框+名字框.png")	
		elif x == 1:
			show_text_name_for_4("神谷   智則")
			show_text_1("辛苦囉，這位是御影翔平，交個朋友吧～")
		elif x == 2:
			original_board("教室+好朋友和女主+對話框+名字框.png")
			x += 1
		elif x == 3:
			show_text_name_for_4("御影   翔平")
			show_text_1("哈囉哈囉~")
		elif x == 4:
			original_board("教室+好朋友和女主+對話框+名字框.png")
			x += 1
		elif x == 5:
			show_text_name_for_4("榊原   凜")
			show_text_1("嗨，智則應該沒太騷擾你吧")
		elif x == 6:
			original_board("教室+好朋友和女主+對話框+名字框.png")
		elif x == 7:
			show_text_name_for_4("神谷   智則")
			show_text_1("我們高中同班，算老友了吧。她現在單身，目標好像是一學期交一個男友的樣子。")
		elif x == 8:
			original_board("教室+好朋友和女主+對話框+名字框.png")
		elif x == 9:
			show_text_name_for_4("榊原   凜")
			show_text_1("跟你考上同系真衰哈哈，你不要玩到被當再來找我求救就好。")
		elif x == 10:
			show_text_2("翔平，要是以後智則跟你講什麼幹話你就嗆爆他不用客氣xD")
		elif x == 11:
			original_board("教室+好朋友和女主+對話框+名字框.png")
			x += 1
		elif x == 12:
			show_text_name_for_4("御影   翔平")
		elif x == 13:
			button_for_chapter("兩位關係真不錯，我在這都沒認識的人哈哈",100, 580, 800, 30, 2, dark_gray, black, whattodo = "兩位關係真不錯，我在這都沒認識的人哈哈")
			button_for_chapter("真假，為什麼不用客氣啊，客氣不好嗎==", 100, 620, 800, 30, 2, dark_gray, black, whattodo = "真假，為什麼不用客氣啊，客氣不好嗎==")
			button_for_chapter("那他講幹話的時候我嗆爆妳可以嗎", 100, 660, 800, 30, 2, dark_gray, black, whattodo = "那他講幹話的時候我嗆爆妳可以嗎")
		if x > 13:
			x = 13
		if z == 1:
			change_background("教室+好朋友和女主+對話框+名字框.png", "教室+好朋友和女主+對話框+名字框.png", 30)
			par += 1
			x = 0
			
			
	elif par == 15 and choice == 1:
		theblock_for_changing_background = 4 + 1
		z = 0
		if x == 0:
			original_board("教室+好朋友和女主+對話框+名字框.png")	
		elif x == 1:
			show_text_name_for_4("榊原   凜")
			show_text_1("沒事，以後有事可以找我們，沒事也可以。")
		elif x == 2:
			original_board("教室+好朋友和女主+對話框+名字框.png")
		elif x == 3:
			show_text_name_for_4("神谷   智則")
			show_text_1("我覺得不行。")
		elif x == 4:
			change_background("教室+好朋友和女主+對話框+名字框.png", "教室+對話框.png", 30)
			par += 1
			x = 0
			
			
	elif par == 15 and choice == 2:
		theblock_for_changing_background = 8 + 1
		z = 0
		if x == 0:
			original_board("教室+好朋友和女主+對話框+名字框.png")
		elif x == 1:
			show_text_name_for_4("榊原   凜")
			show_text_1("對齁，有道理欸！你邏輯是不是還不錯啊==")
		elif x == 2:
			original_board("教室+好朋友和女主+對話框+名字框.png")
		elif x == 3:
			show_text_name_for_4("御影   翔平")
			show_text_1("還好啦，就if跟else而已啊~")
		elif x == 4:
			original_board("教室+好朋友和女主+對話框+名字框.png")
		elif x == 5:
			show_text_name_for_4("神谷   智則")
			show_text_1("對啊，這樣就停修也太玻璃了吧")
		elif x == 6:
			original_board("教室+好朋友和女主+對話框+名字框.png")
		elif x == 7:
			show_text_name_for_2("三人")
			show_text_1("哈哈哈哈哈哈哈哈哈哈")
		elif x == 8:
			change_background("教室+好朋友和女主+對話框+名字框.png", "教室+對話框.png", 30)
			par += 1
			x = 0
			
			
	elif par == 15 and choice == 3:
		theblock_for_changing_background = 4 + 1
		z = 0
		if x == 0:
			original_board("教室+好朋友和女主+對話框+名字框.png")
		elif x == 1:
			show_text_name_for_4("榊原   凜")
			show_text_1("好問題欸，等，我想一下==")
		elif x == 2:
			original_board("教室+好朋友和女主+對話框+名字框.png")
		elif x == 3:
			show_text_name_for_4("神谷   智則")
			show_text_1("哇塞，你把在場所有人都嗆過一遍也沒問題吧？")
		elif x == 4:
			change_background("教室+好朋友和女主+對話框+名字框.png", "教室+對話框.png", 30)
			par += 1
			x = 0
			
			
	elif par == 16:
		theblock_for_changing_background = 3 + 1
		if x == 0:
			original_board("教室+對話框.png")
		elif x == 1:
			show_text_1("簡單聊了幾句...")
			show_text_2("姑且算是認識了兩位同學吧，超乎預期的多呢。")
		elif x == 2:
			show_text_4("（第一堂課結束）")
		elif x == 3:
			change_background("教室+對話框.png", "黒+對話框.png", 30)
			par += 1
			x = 0

			
	elif par == 17:
		theblock_for_changing_background = 9 + 1
		if x == 0:
			original_board("黒+對話框.png")
		elif x == 1:
			show_text_1("(過了一些日子)")
		elif x == 2:
			original_board("黒+對話框.png")
		elif x == 3:
			show_text_1("原以為上了大學脫離家裡，生活會改變許多。")			
		elif x == 4:
			show_text_2("其實也真的還好，或許個性上我就是比較獨立吧。")
		elif x == 5:
			original_board("黒+對話框.png")
		elif x == 6:
			show_text_1("不管怎麼樣，開學也快一個月了，差不多習慣了這裡的生活，")
		elif x == 7:
			original_board("黒+對話框.png")
		elif x == 8:
			show_text_1("系上的氣氛也漸漸活絡起來了。")
		elif x == 9:
			change_background("黒+對話框.png", "街頭+好朋友+對話框+名字框.png", 30)
			par += 1
			x = 0
			
	elif par == 18:	
		theblock_for_changing_background = 7 + 1
		if x == 0:
			original_board("街頭+好朋友+對話框+名字框.png")
		elif x == 1:
			show_text_name_for_4("神谷   智則")
			show_text_1("周末有空嗎？要不要一起出去逛逛？")
		elif x == 2:
			original_board("街頭+好朋友+對話框.png")
		elif x == 3:
			show_text_1("開學以來多少也記住了幾位同學的名字，不過比較常往來的還是只有智則和凜。")
		elif x == 4:
			original_board("街頭+好朋友+對話框.png")
		elif x == 5:
			show_text_1("智則是熱情的人，不過…該去嗎？")
		elif x == 6:
			original_board("街頭+好朋友+對話框.png")
		elif x == 7:
			button_for_chapter("剛好沒甚麼事，就出去逛逛吧",100, 580, 800, 30, 2, dark_gray, black, whattodo = "剛好沒甚麼事，就出去逛逛吧")
			button_for_chapter("在宿舍讀書好了", 100, 620, 800, 30, 2, dark_gray, black, whattodo = "在宿舍讀書好了")
		if x > 7:
			x = 7
		if z == 1:
			change_background("街頭+好朋友+對話框.png", "街頭+好朋友+對話框+名字框.png", 30)
			par += 1
			x = 0
			
			
	elif par == 19 and choice == 1:	
		theblock_for_changing_background = 4 + 1
		z = 0
		if x == 0:
			original_board("街頭+好朋友+對話框+名字框.png")
		elif x == 1:
			show_text_name_for_4("神谷   智則")
			show_text_1("耐斯，那就到時候見囉！")
		elif x == 2:
			original_board("街頭+對話框.png")
		elif x == 3:
			show_text_1("要拒絕他還真有點不好意思，現在也沒什麼心情念書，出去散散心也好吧。")
		elif x == 4:
			change_background("街頭+對話框.png", "blackintro.png", 30)
			par += 1
			x = 0
			
	elif par == 19 and choice == 2:	
		theblock_for_changing_background = 33 + 1
		z = 0
		if x == 0:
			original_board("街頭+好朋友+對話框+名字框.png")
		elif x == 1:
			show_text_name_for_4("神谷   智則")
			show_text_1("好吧，我好像也應該讀點書……")
		elif x == 2:
			original_board("街頭+好朋友+對話框+名字框.png")
		elif x == 3:
			show_text_name_for_4("神谷   智則")
			show_text_1("沒有啦，我亂講的== 改天有空一起出來吧。")
		elif x == 4:
			original_board("街頭+對話框.png")
		elif x == 5:
			show_text_1("其實拒絕他還滿不好意思的，")
		elif x == 6:
			original_board("街頭+對話框.png")
		elif x == 7:
			show_text_1("不過也不確定自己是不是真的想和沒那麼熟的人出去。")
		elif x == 8:
			original_board("街頭+對話框.png")
		elif x == 9:
			show_text_1("該念的書還是得念吧，都進這間學校了......")
		elif x == 10:
			change_background("街頭+對話框.png", "宿舍+對話框.png", 30)
			x += 1
		elif x == 11:
			original_board("宿舍+對話框.png")
		elif x == 12:
			show_text_1("(放下會計課本休息一下...)")
		elif x == 13:
			original_board("宿舍+對話框.png")
		elif x == 14:
			show_text_1("不知道智則今天去哪玩了呢？")
		elif x == 15:
			original_board("宿舍+對話框.png")
			x += 1
		elif x == 16:
			show_text_1("開學到現在，其實並不排斥這科系要學的科目，")
		elif x == 17:
			show_text_2("但也不確定是不是真的喜歡。")
		elif x == 18:
			show_text_3("大概也是得走過才知道路有多崎嶇，")
		elif x == 19:
			show_text_4("還是別抱怨了吧。")
		elif x == 20:
			original_board("宿舍+對話框.png")
		elif x == 21:
			show_text_1("好了，下一科。")
		elif x == 22:
			change_background("宿舍+對話框.png", "黒+對話框.png", 30)
			x += 1
		elif x == 23:
			original_board("黒+對話框.png")
		elif x == 24:
			show_text_1("線性代數好難啊。")
		elif x == 25:
			original_board("黒+對話框.png")
		elif x == 26:
			show_text_1("進行投影")
			show_text_2("是因為不是每個問題都有解答")
		elif x == 27:
			original_board("黒+對話框.png")
		elif x == 28:
			show_text_1("限制式多")
			show_text_2("而能控制的變數太少")
			show_text_3("就像想用單一的顏色畫出這座城市")
		elif x == 29:
			original_board("黒+對話框.png")
		elif x == 30:
			show_text_1("或許我們所有人或多或少都不屬於這個空間")
		elif x == 31:
			show_text_2("而我們還是努力地在這個世界")
		elif x == 32:
			show_text_3("尋求那個屬於我們的最佳投影。")
		elif x == 33:
			change_background("黒+對話框.png", "blackintro.png", 30)
			par += 1
			x = 0
			goch1 = False	

		


def chapter_2():
	global x, goch2, par, theblock_for_changing_background, playmusic, playmusic2, nowplaying, musicfrom, choice, z
	
	if par == 1:
		theblock_for_changing_background = 13 + 1
		if x == 0:
			original_board("小街+對話框.png")
		elif x == 1:
			show_text_1("這天吃完早餐準備去上課，")
		elif x == 2:
			show_text_2("走著走著，發現前方路上有張學生證。")
		elif x == 3:
			original_board("小街+對話框.png")
			x += 1
		elif x == 4:
			show_text_1("B0X70XXXX，XXX，照片是個男生，從學號看應該和我一樣是管院的人。")
		elif x == 5:
			original_board("小街+對話框.png")
			x += 1
		elif x == 6:
			show_text_1("這個嘛…我應該要…")
		elif x == 7:#button
			original_board("小街+對話框.png")
			x += 1
		elif x == 8:
			show_text_1("物歸原位(丟回去)")
			show_text_2("先收著")
			show_text_3("PO學校交流板")
		elif x == 9:#選項一
			original_board("小街+對話框.png")
			x += 1
		elif x == 10:
			show_text_1("放著吧，這張學生證終究會回到屬於它的地方。")
		elif x == 11:
			original_board("小街+對話框.png")
			x += 1
		elif x == 12:
			show_text_1("總之先進教室吧。")			
		elif x == 13:
			change_background("小街+對話框.png", "教室+對話框.png", 30)
			par += 1
			x = 0
			goch2 = False



			
def chapter_3():
	global x, goch3, par

	
	if par == 1:
		if x == 0:
			original_board("clock.jpg")
		elif x == 1:
			show_text_1("123456789")
		elif x == 2:
			show_text_2("你好嗎?")
		elif x == 3:
			show_text_3("nice to meet you!")
		elif x == 4:
			show_text_4("はじめましで")
		elif x == 5:
			change_background("clock.jpg", "arc.jpg", 30)
			par += 1
			x = 0
			
			
			
	elif par == 2:	
		if x == 0:
			original_board("arc.jpg")
		elif x == 1:
			show_text_1("我叫~~~")
		elif x == 2:
			show_text_2("*'`!~~~~~")
		elif x == 3:
			show_text_3("say yes")
		elif x == 4:
			show_text_4("こんにちは")
		elif x == 5:
			change_background("arc.jpg", "mizuumi.jpg", 30)
			x = 0
			goch3 = False
			

def chapter_8():
	global x, goch8, par, theblock_for_changing_background, playmusic, playmusic2, nowplaying, musicfrom, choice, z
	
	

data = list()

gameExit = False
x = 0	
par = 1
chapter_pointer = 1

choice = 0
z = 0

playmusic = True
playmusic2 = True

goch1 = True
goch2 = True
goch3 = True
goch4 = True
goch5 = True
goch8 = True
	
musicfrom = 0.000
nowplaying = ""
				



pygame.mixer.music.load("sinners.wav")
nowplaying = "sinners.wav"

pygame.mixer.music.load(nowplaying)
pygame.mixer.music.play(-1, musicfrom)



intro_delay_time = 600
intro_change_speed = 48

original_board("blackintro.png")
change_background("blackintro.png", "sakura.jpg", 20)
background_file = "sakura.jpg"
original_board(background_file)
pygame.time.delay(intro_delay_time)
original_board(background_file)
change_background("sakura.jpg", "aniback.jpg", intro_change_speed)

background_file = "aniback.jpg"
original_board(background_file)
pygame.time.delay(intro_delay_time)
original_board(background_file)
change_background("aniback.jpg", "mizuumi.jpg", intro_change_speed)

background_file = "mizuumi.jpg"
original_board(background_file)
pygame.time.delay(intro_delay_time)
original_board(background_file)
change_background("mizuumi.jpg", "clock.jpg", intro_change_speed)

background_file = "clock.jpg"
original_board(background_file)
pygame.time.delay(intro_delay_time)
original_board(background_file)
change_background("clock.jpg", "arc.jpg", intro_change_speed)

background_file = "arc.jpg"
original_board(background_file)
pygame.time.delay(intro_delay_time)
original_board(background_file)
change_background("arc.jpg", "校園+對話框.png", intro_change_speed)

background_file = "校園+對話框.png"
original_board(background_file)
pygame.time.delay(intro_delay_time)
original_board(background_file)
change_background("校園+對話框.png", "blackintro.png", 40)

background_file = "blackintro.png"
original_board(background_file)
change_background("blackintro.png", "start.png", 22)				

background_file = "start.png"
background = pygame.image.load(background_file).convert()

original_board(background_file)
loading()
#main loop

original_board(background_file)
pygame.display.flip()

print(musicfrom)	




while not gameExit:
	clock.tick(60)
	
	
	
	if x > theblock_for_changing_background:
		x = theblock_for_changing_background - 1
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				saving()
			if event.key == pygame.K_d:
				x += 1
			if event.key == pygame.K_a:
				x -= 1
				if x < 0:
					x = 0
	


	
	#game logic
	if chapter_pointer == 1 and goch1 == True:	
		chapter_1()
	elif chapter_pointer == 1 and goch1 == False:
		x = 0
		par = 1
		chapter_pointer = 2
	
	
	if chapter_pointer == 2 and goch2 == True:
		chapter_2()
	elif chapter_pointer == 2 and goch2 == False:
		x = 0
		par = 1
		chapter_pointer = 3
	
	
	if chapter_pointer == 3 and goch3 == True:
		chapter_3()
	elif chapter_pointer == 3 and goch3 == False:
		x = 0
		par = 1
		chapter_pointer = 4
	
	
	if chapter_pointer == 4 and goch3 == True:
		chapter_3()
	elif chapter_pointer == 4 and goch3 == False:
		x = 0
		par = 1
		chapter_pointer = 5
		
	
	if chapter_pointer == 5 and goch3 == True:
		chapter_3()
	elif chapter_pointer == 5 and goch3 == False:
		x = 0
		par = 1
		chapter_pointer = 8
	
	
	if chapter_pointer == 8 and goch3 == True:
		chapter_3()
	elif chapter_pointer == 8 and goch3 == False:
		x = 0
		par = 1
		chapter_pointer = 9
	
		
		

#test again




	
pygame.quit()
quit()
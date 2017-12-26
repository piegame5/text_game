import pygame
import time

pygame.init()

pygame.font.get_fonts()

pygame.mixer.music.load("cr_music.mp3")
#crowd_sound = pygame.mixer.Sound("cr_music.mp3")

red = (255,0,0)
white = (255,255,255)
black = (0,0,0)

screen_width = 1280
screen_height = 720

screen = pygame.display.set_mode((screen_width, screen_height))
#screen = pygame.display.set_mode((1024,768))
pygame.display.set_caption('testing game')

pygame.display.update()

gameExit = False

clock = pygame.time.Clock()

background_file = "sakura.jpg"
background = pygame.image.load(background_file).convert()

font = pygame.font.SysFont('mingliupmingliumingliuhkscs',25)

theblock_for_changing_background = 6
	
def message_to_screen(msg,color,x,y):
	screen_text = font.render(msg,True,color)
	screen.blit(screen_text,[x,y])
	
def show_text_1(text1):
	message_to_screen(text1,black,25,550)
	pygame.display.update()
	
def show_text_2(text2):
	message_to_screen(text2,black,25,590)
	pygame.display.update()
	
def show_text_3(text3):
	message_to_screen(text3,black,25,630)
	pygame.display.update()
	
def show_text_4(text4):
	message_to_screen(text4,black,25,670)
	pygame.display.update()
	
def original_board(background_file):
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
	global screen
	
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


def chapter_1():
	global x, goch1, par, theblock_for_changing_background, playmusic, playmusic2
	
	
	
	if par == 1:
		theblock_for_changing_background = 12 + 1
		
		if playmusic == True:
			pygame.mixer.music.play(-1)
			playmusic = False
			
		if x == 0:
			original_board("sakura.jpg")
		elif x == 1:
			show_text_1("曾幾何時，我們睜開眼不再做夢，夢只能隱晦的收藏？")
		elif x == 2:
			show_text_2("曾幾何時，空白筆記填滿的是數學公式，而非一條蛇吞了大象？")
		elif x == 3:
			show_text_3("我不是我，我是一張張成績單。專心讀書，進好大學出社會，當個成功的人，幸福就會不請自來。")
		elif x == 4:
			show_text_4("大人是這樣說的，所以我這樣做。")
		elif x == 5:
			original_board("sakura.jpg")
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
			original_board("sakura.jpg")
		elif x == 11:
			show_text_1("說得好像我有得選一樣。")
		elif x == 12:
			change_background("sakura.jpg", "aniback.jpg", 30)
			par += 1
			x = 0
	
	
	

	elif par == 2:
		theblock_for_changing_background = 21 + 1
		
		if playmusic2 == True:
			pygame.mixer.music.fadeout(1000)
			pygame.mixer.music.load("kara_m01.mp3")
			pygame.mixer.music.play(-1)
			playmusic2 = False
			
			
		if x == 0:
			original_board("aniback.jpg")
		elif x == 1:
			show_text_1("開學典禮")
		elif x == 2:
			original_board("aniback.jpg")
			#pygame.mixer.Sound.play(crowd_sound)
		elif x == 3:
			show_text_1("校長：")
		elif x == 4:
			show_text_2("歡迎來到__大學！")
		elif x == 5:
			show_text_3("在這令人興奮的時刻，我在台上看到的是一朵朵生機盎然的嫩芽，渴望著養分灌溉。")
		elif x == 6:
			show_text_4("本校是何其榮幸，能做為孕育優秀如你們的搖籃。")
		elif x == 7:
			original_board("aniback.jpg")
			x += 1
		elif x == 8:
			show_text_1("校長：")
		elif x == 9:
			show_text_2("從收到入學通知書的那一刻起，你們就代表了本校，和本校的未來。")
		elif x == 10:
			show_text_3("今日你以__大為榮，他日__大將以你為榮，恭喜各位！")
		elif x == 11:
			original_board("aniback.jpg")
			x += 1
		elif x == 12:
			show_text_1("校長：")
		elif x == 13:
			show_text_2("我們來自不同的地方，有著不同的背景，一個人的際遇造就了現在的自己，而我們現在齊聚在這裡。")
		elif x == 14:
			show_text_3("你們想成為怎麼樣的人呢？我期待你們能在這階段結交好友，成就自己。")
		elif x == 15:
			show_text_4("你也許會困惑，你一定會遇到困難，但請記得你並不是一個人。")
		elif x == 16:
			original_board("aniback.jpg")
			x += 1
		elif x == 17:
			show_text_1("校長：")
		elif x == 18:
			show_text_2("大學是各位一生至關重要的階段，一個人的選擇，編織了一段段不同的人生，串聯起一篇篇精彩的故事。")
		elif x == 19:
			show_text_3("請尊重引導你們的師長，謹言慎行、服從校規。")
		elif x == 20:
			show_text_4("當你們面臨進行重大抉擇的時刻，請務必慎重，並為自己的選擇負起責任。")
		elif x == 21:
			original_board("aniback.jpg")
			par += 1
			x = 0
			
	elif par == 3:
		theblock_for_changing_background = 5 + 1
		if x == 0:
			original_board("aniback.jpg")
		elif x == 1:
			show_text_1("所有校長都有的共通點，廢話特多，而且都是老爺爺。校長上台開講已經有20分鐘，感覺還要一陣子。")
		elif x == 2:
			show_text_2("大部分的學生都已經沒有耐心聽演講，有些開始滑手機，有些開始和身邊的人搭訕自我介紹。")
		elif x == 3:
			show_text_3("入學第一天除了參加入學典禮也沒有其他事情會發生。我百無聊賴地拿出手機滑了起來。")
		elif x == 4:
			show_text_4("(開學典禮結束)")
		elif x == 5:
			change_background("aniback.jpg", "mizuumi.jpg", 30)
			par += 1
			x = 0
			
			
			
	elif par == 4:
		theblock_for_changing_background = 7 + 1
		if x == 0:
			original_board("mizuumi.jpg")
		elif x == 1:
			show_text_1("（第一堂課）")
		elif x == 2:
			original_board("mizuumi.jpg")
		elif x == 3:
			show_text_1("第一堂課，周圍坐的系上同學大約也有上百位...我們真算是一個大系，想到要記起這上百人的名字就覺得麻煩。")
		elif x == 4:
			show_text_2("教室是個階梯式講堂，高中時也只有在大一點的特殊教室或補習班才看的到這種形式。")
		elif x == 5:
			show_text_3("雖然人數眾多，教室內的氣氛大致是低迷的，只有少數互相認識的人低聲交談。")
		elif x == 6:
			show_text_4("這時多少會覺得要是身旁有個認識的人就好了，有誰想得到此時此刻我會坐在這裡呢?")
		elif x == 7:
			original_board("mizuumi.jpg")
			par += 1
			x = 0
			
			
	elif par == 5:
		theblock_for_changing_background = 10 + 1
		if x == 0:
			original_board("mizuumi.jpg")
		elif x == 1:
			show_text_1("教授：「同學們請安靜坐好，開始上課囉」")
		elif x == 2:
			original_board("mizuumi.jpg")
		elif x == 3:
			show_text_1("看起來年約五六十的教授走進教室，身材有些臃腫。")
		elif x == 4:
			show_text_2("偏圓的臉，黝黑的肌膚和所剩不多的白髮訴說著歲月，但並不影響他的意氣風發。")
		elif x == 5:
			original_board("mizuumi.jpg")
			x += 1
		elif x == 6:
			show_text_1("教授：")
		elif x == 7:
			show_text_2("還是不免俗地說一句歡迎各位來到__大學。在剛脫離升學壓力，迎接新生活的階段，我明白大家都還是很亢奮的。")
		elif x == 8:
			show_text_3("但我也要勸各位盡早收起浮躁，好好努力才是真的。")
		elif x == 9:
			show_text_4("教授在大學時代，大家都在辦活動在玩的時候，我總是一個人在圖書館．．．．．．")
		elif x == 10:
			original_board("mizuumi.jpg")
			par += 1
			x = 0
			
			
	elif par == 6:
		theblock_for_changing_background = 7 + 1
		if x == 0:
			original_board("mizuumi.jpg")
		elif x == 1:
			show_text_1("教授開始說起當年他是如何寒窗十年無人問、取得今日規模的成就、羨煞多少浮世眾生．．．．．．")
		elif x == 2:
			show_text_2("又扯一些什麼沒實力就等淘汰啊、什麼人脈很重要啊、眼光放遠才能獲得最大利益等等等等。")
		elif x == 3:
			original_board("mizuumi.jpg")
			x += 1
		elif x == 4:
			show_text_1("天啊，管院的人都這樣嗎？")
		elif x == 5:
			show_text_2("我以後會變得和他一樣嗎？")
		elif x == 6:
			show_text_3("現在回頭太遲了嗎？")
		elif x == 7:
			original_board("mizuumi.jpg")
			par += 1
			x = 0
			
	elif par == 7:
		theblock_for_changing_background = 9 + 1
		if x == 0:
			original_board("mizuumi.jpg")
		elif x == 1:
			show_text_1("教授：")
		elif x == 2:
			show_text_2("．．．．．．以後進了職場，一個重要的能力就是和人群說話，那就是我們今天要做的事啦。")
		elif x == 3:
			show_text_3("請大家上台用一分鐘介紹你自己，下次再開始上正課。")
		elif x == 4:
			original_board("mizuumi.jpg")
		elif x == 5:
			show_text_1("教授拿出事先護貝好的名牌，讓大家能看清楚接下來上台的人的名字。")
		elif x == 6:
			show_text_2("第一堂課就是上百人一個一個自我介紹，")
		elif x == 7:
			show_text_3("這種方式雖然對認識人沒什麼幫助，但似乎也沒有更好的方法了。")
		elif x == 8:
			show_text_4("一開始大家都還試著掰出一分鐘的長度，後來漸漸地大家就開始無視這規則了......而我也是這麼打算的。")
		elif x == 9:
			original_board("mizuumi.jpg")
			par += 1
			x = 0
	
	
	elif par == 8:
		theblock_for_changing_background = 38 + 1
		if x == 0:
			original_board("mizuumi.jpg")
		elif x == 1:
			show_text_1("「我叫__，來自__，希望能和大家好好相處啦，請多指教」")
		elif x == 2:
			original_board("mizuumi.jpg")
		elif x == 3:
			show_text_1("台下響起些微意思性的掌聲送我回到座位，")
		elif x == 4:
			show_text_2("正當我想繼續滑手機時，")
		elif x == 5:
			show_text_3("後方傳來一句男聲。")
		elif x == 6:
			original_board("mizuumi.jpg")
			x += 1
		elif x == 7:
			show_text_1("？？：「這堂課還真奇怪，對吧？」")
		elif x == 8:
			original_board("mizuumi.jpg")
		elif x == 9:
			show_text_1("回頭一看，一個帶著粗框眼鏡的帥氣男孩笑咪咪地看著我。")
		elif x == 10:
			original_board("mizuumi.jpg")
		elif x == 11:
			show_text_1("好朋友1：")
			show_text_2("「我叫___，___(主角名)，請多指教。」")
		elif x == 12:
			original_board("mizuumi.jpg")
		elif x == 13:
			show_text_1("「喔喔嗨，很高興認識你。」")
			show_text_2("我回答道")
		elif x == 14:
			original_board("mizuumi.jpg")
			x += 1
		elif x == 15:
			show_text_1("＿＿看起來就是那種幽默開朗，大家看到都會喜歡的那種人。")
		elif x == 16:
			show_text_2("可能只是想找個人聊天吧...")
		elif x == 17:
			original_board("mizuumi.jpg")
		elif x == 18:
			show_text_1("好朋友1：")
			show_text_2("「這個學校真的很棒，聽說畢業生的就業率是完美的100%，而且畢業生全都進入了很不錯的大公司耶！」")
		elif x == 19:
			original_board("mizuumi.jpg")
		elif x == 20:
			show_text_1("我：")
			show_text_2("「這樣啊，我想大家都是一樣看上這點的吧」")
		elif x == 21:
			original_board("mizuumi.jpg")
		elif x == 22:
			show_text_1("那我是為了什麼進這間學校的呢？")
		elif x == 23:
			original_board("mizuumi.jpg")
		elif x == 24:
			show_text_1("好朋友1：")
			show_text_2("「對阿，大家都希望能順利畢業並成功就業呢。對了你看，現在在台上的是我朋友」")
		elif x == 25:
			original_board("mizuumi.jpg")
		elif x == 26:
			show_text_1("現在在台上的是一個女生。")
		elif x == 27:
			show_text_2("說話有點小聲，卻不是怯懦的那種，反倒給人一種無法忽視她存在的感覺。")
		elif x == 28:
			show_text_3("介紹完後，她朝我們這邊走過來。")
		elif x == 29:
			original_board("mizuumi.jpg")
		elif x == 30:
			show_text_1("好朋友1：")
			show_text_2("「辛苦囉，這位是____(主角名)，一起交個朋友吧」")
		elif x == 31:
			original_board("mizuumi.jpg")
			x += 1
		elif x == 32:
			show_text_1("我：")
			show_text_2("「哈囉哈囉」")
		elif x == 33:
			original_board("mizuumi.jpg")
			x += 1
		elif x == 34:
			show_text_1("女主角：")
			show_text_2("「嗨，____(好朋友1)應該沒太騷擾你吧」")
		elif x == 35:
			original_board("mizuumi.jpg")
		elif x == 36:
			show_text_1("簡單聊了幾句，對話也沒進行下去了。")
			show_text_2("姑且算是認識了兩位同學吧，超乎預期的多呢。")
		elif x == 37:
			show_text_4("（第一堂課結束）")
		elif x == 38:
			change_background("mizuumi.jpg", "clock.jpg", 30)
			par += 1
			x = 0
			
	elif par == 9:
		theblock_for_changing_background = 6 + 1	
		if x == 0:
			original_board("clock.jpg")
		elif x == 1:
			show_text_1("（過了一些日子）")
		elif x == 2:
			original_board("clock.jpg")
		elif x == 3:
			show_text_1("原以為上了大學脫離家裡，生活會改變許多。其實也真的還好，或許個性上我就是比較獨立，")
		elif x == 4:
			show_text_2("又或許我其實早已脫離那個家也說不定。")
		elif x == 5:
			show_text_3("不管怎麼樣，開學也快一個月了，差不多習慣了這裡的生活，系上的人們也漸漸活絡起來了。")
		elif x == 6:
			change_background("clock.jpg", "arc.jpg", 30)
			par += 1
			x = 0
			
	elif par == 10:
		theblock_for_changing_background = 6 + 1	
		if x == 0:
			original_board("arc.jpg")
		elif x == 1:
			show_text_1("好朋友1：")
			show_text_2("「對了，你等會兒有空嗎？要不要一起出去玩玩？我住在這個附近我帶你去認識這個地方」")
		elif x == 2:
			original_board("arc.jpg")
			x += 1
		elif x == 3:
			show_text_1("要不要跟他出去玩呢...?")
		elif x == 4:
			show_text_2("1.也好，晚上剛好也沒甚麼事，就出去玩玩交朋友吧~    回答好朋友1：好啊~")
			show_text_3("2.不要好了，暫時不想和人有太多接觸")
		elif x == 6:
			original_board("arc.jpg")
			par += 1
			x = 0		
			goch1 = False	

			


def chapter_2():
	global x, goch2, par
	
	if par == 1:
		if x == 0:
			original_board("mizuumi.jpg")
		elif x == 1:
			show_text_1("哈囉")
		elif x == 2:
			show_text_2("你好嗎?")
		elif x == 3:
			show_text_3("nice to meet you!")
		elif x == 4:
			show_text_4("はじめましで")
		elif x == 5:
			change_background("mizuumi.jpg", "clock.jpg", 30)
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

x = 0	
par = 1
chapter_pointer = 1	
playmusic = True
playmusic2 = True

goch1 = True
goch2 = True
goch3 = True	

#main loop
while not gameExit:
	clock.tick(60)
	
	
	
	if x > theblock_for_changing_background:
		x = theblock_for_changing_background - 1
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True
		if event.type == pygame.KEYDOWN:
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
	
		
		
	
#test again


	
pygame.quit()
quit()
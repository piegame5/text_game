def chapter_3():
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
			button_for_chapter("物歸原位(丟回去)",100, 580, 800, 30, 2, dark_gray, black, whattodo = "物歸原位(丟回去)")
			button_for_chapter("先收著", 100, 620, 800, 30, 2, dark_gray, black, whattodo = "先收著")
			button_for_chapter("PO學校交流板", 100, 660, 800, 30, 2, dark_gray, black, whattodo = "PO學校交流板")
		if x > 8:
			x = 8
		if z == 1:
			change_background("小街+對話框.png", "小街+對話框.png", 30)
			par += 1
			x = 0
			
	elif par == 2:
		theblock_for_changing_background = 3 + 1
		z = 0
		if x == 1:
			original_board("小街+對話框.png")
			x += 1
		elif x == 2:
			show_text_1("總之先進教室吧。")			
		elif x == 3:
			change_background("小街+對話框.png", "教室+對話框.png", 30)
			par += 1
			x = 0
			
	elif par == 3:
		theblock_for_changing_background = 2 + 1
		if x == 0:
			original_board("教室+對話框.png")
		elif x == 1:
			show_text_1("課上到一半，有人拍了拍我的肩膀")
		elif x == 2:
			change_background("教室+對話框.png", "教室+女主+對話框+名字框.png", 30)
			par += 1
			x = 0
	
	
	elif par == 4:
		theblock_for_changing_background = 30 + 1
		if x == 0:
			original_board("教室+女主+對話框+名字框.png")
			x += 2
		elif x == 2:
			show_text_name_for_4("榊原   凜")
			show_text_1("這裡有人坐嗎？")
		elif x == 3:
			original_board("教室+女主+對話框+名字框.png")
			x += 1
		elif x == 4:
			show_text_1("凜突然從我後面出現，挑了我旁邊的位置坐下來。")
		elif x == 5:
			original_board("教室+女主+對話框+名字框.png")
			x += 1
		elif x == 6:
			show_text_name_for_4("御影   翔平")
			show_text_1("怎樣，睡過頭喔？")
		elif x == 7:
			original_board("教室+女主+對話框+名字框.png")
			x += 1
		elif x == 8:
			show_text_name_for_4("榊原   凜")
			show_text_1("對啊，昨天就念書念滿晚的。")
		elif x == 9:
			original_board("教室+女主+對話框+名字框.png")
			x += 1
		elif x == 10:
			show_text_name_for_4("榊原   凜")
			show_text_1("上次小考不太好考啊，平均分數竟然不及格，這教授聽說每年都當很多人耶。")
		elif x == 11:
			show_text_2("你上次考多少啊？")
		elif x == 12:
			original_board("教室+女主+對話框+名字框.png")
			x += 1
		elif x == 13:
			show_text_name_for_4("御影   翔平")
			show_text_1("65")
		elif x == 14:
			original_board("教室+女主+對話框+名字框.png")
			x += 1
		elif x == 15:
			show_text_name_for_4("榊原   凜")
			show_text_1("哈，我高你一點，68。不過這樣下去期末有點危險呢。")
		elif x == 16:
			original_board("教室+女主+對話框+名字框.png")
			x += 1
		elif x == 17:
			show_text_name_for_4("御影   翔平")
			show_text_1("我也覺得，大概是得再努力一點才行。就業率100%的學校，還是沒那麼輕鬆吧。")
		elif x == 18:
			original_board("教室+女主+對話框+名字框.png")
			x += 1
		elif x == 19:
			show_text_name_for_4("榊原   凜")
			show_text_1("還是我們來比期末考的分數，輸的請吃飯，怎麼樣？")
		elif x == 20:
			original_board("教室+女主+對話框+名字框.png")
			x += 1
		elif x == 21:
			show_text_name_for_4("御影   翔平")
			show_text_1("可以啊，講得好像妳會贏一樣")
		elif x == 22:
			original_board("教室+女主+對話框+名字框.png")
			x += 1
		elif x == 23:
			show_text_name_for_4("榊原   凜")
			show_text_1("也不想想這次是誰贏了喔，你是不是該先請我點什麼啊？")
		elif x == 24:
			original_board("教室+女主+對話框+名字框.png")
			x += 1
		elif x == 25:
			show_text_name_for_4("御影   翔平")
			show_text_1("請妳什麼？")
		elif x == 26:
			original_board("教室+女主+對話框+名字框.png")
			x += 1
		elif x == 27:
			show_text_name_for_4("榊原   凜")
			show_text_1("我口有點渴，你可以請我冷飲。")
		elif x == 28:
			original_board("教室+女主+對話框+名字框.png")
			x += 1
		elif x == 29:
			show_text_name_for_4("御影   翔平")
			show_text_1("請你老母。")
		elif x == 30:
			change_background("教室+女主+對話框+名字框.png", "教室+對話框.png", 30)
			par += 1
			x = 0
			
			
	elif par == 5:
		theblock_for_changing_background = 2 + 1
		if x == 0:
			original_board("教室+對話框.png")
			x += 1
		elif x == 1:
			show_text_1("(下課鐘聲響起)")
		elif x == 2: #1:ch3結束  2:par +=1 3:par += 3
			if choice == 1:
				change_background("教室+對話框.png", "教室+對話框.png", 30)
				par = 9
				x = 0
			elif choice == 2:
				change_background("教室+對話框.png", "教室+對話框.png", 30)
				par += 1
				x = 0
				choice = 0
			elif choice == 3:
				change_background("教室+對話框.png", "教室+對話框.png", 30)
				par += 3
				x = 0
				choice = 0
			
			
	elif par == 6:
		theblock_for_changing_background = 4 + 1
		if x == 0:
			original_board("教室+對話框.png")
			x += 1
		elif x == 1:
			show_text_1("我拿出學生證開始研究。")
		elif x == 2:
			original_board("教室+對話框.png")
			x += 1
		elif x == 3:
			show_text_1("照片中的男生理著平頭，皮膚偏蒼白，臉有點消瘦，眼窩有點凹陷。")
		elif x == 4:
			change_background("教室+對話框.png", "教室+女主+對話框+名字框.png", 30)
			par += 1
			x = 0
			
			
	elif par == 7:
		theblock_for_changing_background = 12 + 1
		if x == 0:
			original_board("教室+女主+對話框+名字框.png")
			x += 1
		elif x == 1:
			show_text_name_for_4("榊原   凜")
			show_text_1("欸？這是我朋友的學生證，怎麼在你這？")
		elif x == 2:
			original_board("教室+女主+對話框+名字框.png")
			x += 1
		elif x == 3:
			show_text_name_for_4("御影   翔平")
			show_text_1("這個喔，就路上撿到的，你認識他嗎？")
		elif x == 4:
			original_board("教室+女主+對話框+名字框.png")
			x += 1
		elif x == 5:
			show_text_name_for_4("榊原   凜")
			show_text_1("對啊，社團認識的朋友。")
		elif x == 6:
			original_board("教室+女主+對話框+名字框.png")
			x += 1
		elif x == 7:
			show_text_name_for_4("御影   翔平")
			show_text_1("是喔，那他有在吸毒嗎？")
		elif x == 8:
			original_board("教室+女主+對話框+名字框.png")
			x += 1
		elif x == 9:
			show_text_name_for_4("榊原   凜")
			show_text_1("哈哈哈哈他很可憐，長得超像吸毒犯，下次去問他是不是在吸XD 幫你還他嗎？")
		elif x == 10:
			original_board("教室+女主+對話框+名字框.png")
			x += 1
		elif x == 11:
			show_text_name_for_4("御影   翔平")
			show_text_1("主角：哈哈好的，交給妳了。")
		elif x == 12:
			change_background("教室+女主+對話框+名字框.png", "教室+對話框.png", 30)
			par = 9
			x = 0

	elif par == 8:
		theblock_for_changing_background = 19 + 1
		if x == 0:
			original_board("教室+對話框.png")
			x += 1
		elif x == 1:
			show_text_1("下課後我把學生證的照片放到交流版。")
		elif x == 2:
			original_board("教室+對話框.png")
			x += 1
		elif x == 3:
			show_text_1("「XX系XXX，請認識的人幫忙tag他。」")
		elif x == 4:
			original_board("教室+對話框.png")
			x += 1
		elif x == 5:
			show_text_1("底下的留言紛紛串聯起來。")
		elif x == 6:
			original_board("教室+對話框.png")
			x += 1
		elif x == 7:
			show_text_1("「欸你的學生證啦」")
		elif x == 8:
			show_text_2("「怎麼又掉了啊？」")
		elif x == 9:
			show_text_3("「笑死，是不是差點補發第10次啊」")
		elif x == 10:
			original_board("教室+對話框.png")
			x += 1
		elif x == 11:
			show_text_1("不久後那個人就來找我。")
		elif x == 12:
			original_board("教室+對話框.png")
			x += 1
		elif x == 13:
			show_text_1("拿回了學生證，他的眼裡滿是感激。")
		elif x == 14:
			original_board("教室+對話框.png")
			x += 1
		elif x == 15:
			show_text_1("有時候幫助人最棒的回報就是看到這種表情吧，")
		elif x == 16:
			original_board("教室+對話框.png")
			x += 1
		elif x == 17:
			show_text_1("那是失而復得的喜悅。")
		elif x == 18:
			change_background("教室+對話框.png", "教室+對話框.png", 30)
			par = 9
			x = 0
			
	elif par == 9:
		choice = 0
		x = 0
		goch3 = False
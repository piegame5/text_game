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
			print(x)
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
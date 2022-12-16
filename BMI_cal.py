import tkinter as tk

judge_list = ['低体重', '痩せすぎ', '痩せ', '痩せぎみ', '普通体重',
              '過体重', '肥満予備軍', '肥満（1度）', '肥満（2度）', '肥満（3度）']

# メインウィンドウ生成
root = tk.Tk()
#メインウィンドウのサイズ指定
#root.geometry("300x200")
#メインウィンドウの最小サイズを指定
root.minsize(300, 200)
#メインウィンドウの背景色
#root.configure(bg='#ffffff')

# メインウィンドウの設定
root.title("BMI計算")

# 3*5のグリッドを設定
root.columnconfigure(index=0, weight=1)
root.columnconfigure(index=1, weight=1)
root.columnconfigure(index=2, weight=3)
root.rowconfigure(index=0, weight=1)
root.rowconfigure(index=1, weight=1)
root.rowconfigure(index=2, weight=1)
root.rowconfigure(index=3, weight=1)
root.rowconfigure(index=4, weight=1)

# ラベルの配置
text_height = tk.StringVar()
text_height.set("身長：")
label = tk.Label(root, textvariable=text_height)
label.grid(column=0, row=0, sticky='E')

text_cm = tk.StringVar()
text_cm.set('cm')
label = tk.Label(root, textvariable=text_cm)
label.grid(column=2, row=0, sticky='W')

text = tk.StringVar()
text.set("体重：")
label = tk.Label(root, textvariable=text)
label.grid(column=0, row=1, sticky='E')

text_kg = tk.StringVar()
text_kg.set('kg')
label = tk.Label(root, textvariable=text_kg)
label.grid(column=2, row=1, sticky='W')

text_result = tk.StringVar()
text_result.set('あなたのBMI指数は')
label = tk.Label(root, textvariable=text_result)
label.grid(column=0, row=2, sticky='E')

bmi_result = tk.DoubleVar()
bmi_result.set('')
label = tk.Label(root, textvariable=bmi_result)
label.grid(column=1, row=2)

text_judge = tk.StringVar()
text_judge.set('判定は')
label = tk.Label(root, textvariable=text_judge)
label.grid(column=0, row=3, sticky='E')

judge = tk.StringVar()
label = tk.Label(root, textvariable=judge)
label.grid(column=1, row=3)

# テキスト入力欄をメインウィンドウに配置

#身長入力欄
enter_height = tk.DoubleVar()
entry = tk.Entry(root, textvariable=enter_height, bg = 'white', justify="center", width=10)
entry.grid(column=1, row=0)
entry.delete(0, tk.END)

#体重入力欄
enter_weight = tk.DoubleVar()
entry = tk.Entry(root, textvariable=enter_weight, bg = 'white', justify="center", width=10)
entry.grid(column=1, row=1)
entry.delete(0, tk.END)

# イベントハンドラ
def bmi_cal(event):
    global bmi_result
    global judge
    #BMI値を計算
    bmi_result.set('{:.3f}'.format(enter_weight.get() / (enter_height.get() / 100) ** 2))

    #BMI値によってWHO基準の判定を設定
    if bmi_result.get() < 16:
        judge.set(judge_list[0] + '（' + judge_list[1] + '）')
    elif 16 <= bmi_result.get() < 17:
        judge.set(judge_list[0] + '（' + judge_list[2] + '）')
    elif 17 <= bmi_result.get() < 18.5:
        judge.set(judge_list[0] + '（' + judge_list[3] + '）')
    elif 18.5 <= bmi_result.get() < 25:
        judge.set(judge_list[4])
    elif 25 <= bmi_result.get() < 30:
        judge.set(judge_list[5] + '（' + judge_list[6] + '）')
    elif 30 <= bmi_result.get() < 35:
        judge.set(judge_list[7])
    elif 35 <= bmi_result.get() < 40:
        judge.set(judge_list[8])
    elif 40 <= bmi_result.get():
        judge.set(judge_list[9])


# ボタンウィジェットをメインウィンドウに配置、イベントを登録
button = tk.Button(root, text='計算する', bg = '#ffffff', activebackground = '#dddddd')
button.bind("<Button-1>", bmi_cal)
button.grid(column=1, row=4)

# イベントループの開始
root.mainloop()
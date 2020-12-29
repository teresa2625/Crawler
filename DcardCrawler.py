import ssl
import urllib.request as req
import bs4

ssl._create_default_https_context = ssl._create_unverified_context

# Step1. 先 import urllib.request 這個內建的封包，以執行接下來的動作，並且取名為 req ，以方便之後操作。

src = "https://www.dcard.tw/f/softwareengineer"

# 建立一個 request 物件，附加 Request Headers 的資訊——為了讓我們看起來更像一個真正的使用者。（不然 PTT 不會讓我們抓資料。）

request = req.Request(src, headers={
    "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Mobile Safari/537.36"
})

# Step2. 使用 with request.urlopen(網址) 連上網路，並將其重新取名為 response ，最後使用 read() 函數，將網頁結果放入 data 中。

with req.urlopen(request) as response: # 原本 req.urlopen 的括號內會放網址而已，但為了讓我們更像一般使用者，這邊放入剛剛建立的物件。
    data = response.read().decode("utf-8") # 取的網頁的原始碼。並用decode("uyf-8")來翻譯成中文（解碼）。
# print(data) # 取得 PTT 電影版ㄉ網頁原始碼。

# 步驟二：解析原始碼，取得每篇文章的標題。

# 使用第三方套件： beautifulsoup4/直接在終端機打 pip install beautifulsoup4
# debug: 因為是用 macbook ，下載 BS4 相對麻煩些：
# Step1. 將 "curl https://bootstrap.pypa.io/get-pip.py -o get-pip.pysudo python get-pip.py" 貼上終端機。
# Step2. 將 "sudo python get-pip.py" 貼上終端機。 此處將會要求輸入電腦密碼。
# Step3. 下載 pip ，將 "sudo easy_install pip" 貼上終端機。
# Step4. 下載 BS4 ，將 "pip install beautifulsoup4" 貼上終端機。
# Step5. 再次下載 BS4 ，將 "pip3 install beautifulsoup4" 貼上終端機。

# 載入 bs4 套件。

# 利用上方載入套件做解析：變數 data 是剛在網路上抓到的資料，丟給 Beautifulsoup，他會幫我們用 html 解析。 並用 root 代表整份網頁。

root = bs4.BeautifulSoup(data, "html.parser") # 利用上方載入套件做解析：變數 data 是剛在網路上抓到的資料，丟給 beautifulsoup4，他會幫我們用 html 解析。

# 印出網頁，並解透過 "." 來操作要抓取的東西：

# print(root)
# print(root.title) # .title ：抓取網頁標題。<title> 以及 </titl3> 分別代表開始與結束。
# print(root.title.string) # .title.string ：抓取標籤內的文字。(不會再顯示印出上方時句首句末會出現的 <title> 以及 </titl3>)

# 接下來觀察原始碼，看看我們要找的資料有無特別之處：
# 舉例：在 PTT 電影版中，我廟找的每一則文章的標題，在原始碼中都會先被 <a> 夾住 ，再被 <div> 包住。這就是特色！
# 使用 BS4 中強大的套件：
# 下方因為class 是 python 的保留字，程式中不能使用。所以 BeautifulSoup 就選擇使用 class_ 來篩選標籤中的 class 屬性。

# 使用 ".find" 可以幫助我們找到符合一個以下條件的東西：

titles = root.find_all("div", class_="cgoejl-3 fkFjDX") # 尋找 class = "title" 的 div 標籤。
# print(titles) # 印出剛剛上面找到的標籤。這裏 titles 代表上面找到的 div 標籤。
# print(titles[0].string) # 加上 ".a" 代表我們剛剛找到的那個 div 標籤底下的 <a> 裡面的東西； ".string" 則是抓取前面 "titles.a" 抓到的東西的文字。

# 使用 ".find_all" 可以幫助我們找到「全部」符合以下條件的東西：

# titles = root.find_all("div", class_="title") # 尋找所有 class = "title" 的 div 標籤。
# print(titles) # 印出剛剛上面找到的標籤。這裏 titles 代表上面找到的 div 標籤。

# 做完上面動作之後，會發現印出來的資料是一個列表的形式，所以我們嘗試使用 for 迴圈將標題資料抓出來：

for title in titles:
    if title != None: # 因為可能會有內文被刪除的狀況，如果發生則 div 下就不會有 <a> 標籤。所以先用這個判斷式來判斷此狀況是否發生。
        print(title.string) # 如果「不是None」這件事發生，則印出標題（"titles.a" 抓到的東西的文字）。
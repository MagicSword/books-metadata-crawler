Books-metadata-fetcher

# Target

1. 取得 封面圖
2. 書的基本資料
    1 meta data 的就好 get_meta
    2 還是要詳細資料(?)  get_book

requirement
1. requests
2. bs4

[五分鐘理解RESTful API設計](https://medium.com/@jamesshieh0510/%E4%BA%94%E5%88%86%E9%90%98%E7%90%86%E8%A7%A3restful-api%E8%A8%AD%E8%A8%88-14f413b031f7)
```
PUT：更新
PATCH：部分更新
POST：建立
DELETE：刪除
GET：取得
```

```
GET：具有冪等性，相同的查詢請求，不管查詢幾次都應該得到相同的結果。
POST：不具冪等性，相同的建立請求，每次執行，都會建立一個新的資源。
PUT：具冪等性，每次執行更新請求，皆使用同樣的資料覆蓋指定的資源，所以結果不變。
PATCH：不具冪等性，但可以以冪等的方式發出請求。
DELETE：具冪等性，刪除資源後，無論重複多少次刪除，也不會改變結果。
```

輸入
1. ISBN
2. books book id


輸出
1. json



# Data

書
https://www.books.com.tw/products/0010836923

標頭
`#header_id`


breadcrumb
`/html/body/ul`

主要內容
`/html/body/div[4]`


* 書名：如何像電腦科學家一樣思考
* 原文名稱：Think Julia
* 語言：繁體中文，ISBN：9789865023003
* 頁數：324
* 出版社：歐萊禮
* 作者：Ben Lauwens,Allen B. Downey
* 譯者：楊新章
* 出版日期：2019/10/14
* 類別：電腦資訊


書本頁面有SEO的 Meta tag
1. 直接用 Meta 的資料
2. 爬內文

差別：

/html/body/div[4]/div/div[1]/div[2]/div[1]
```
如何像電腦科學家一樣思考
Think Julia
```
/html/body/div[4]/div/div[1]/div[2]/div[2]

```
作者： Ben Lauwens, Allen B. Downey  
 新功能介紹
譯者： 楊新章
出版社：歐萊禮  
 新功能介紹
出版日期：2019/10/14
語言：繁體中文
```

/html/body/div[4]/div/div[2]

/html/body/div[4]/div/div[2]/div[1]/div[1]
內容簡介

/html/body/div[4]/div/div[2]/div[1]/div[2]
作者簡介 

/html/body/div[4]/div/div[2]/div[1]/div[3]
目錄

/html/body/div[4]/div/div[2]/div[1]/div[4]
詳細資料

```
ISBN：9789865023003
規格：平裝 / 324頁 / 18.5 x 23 x 1.62 cm / 普通級 / 單色印刷 / 初版
出版地：台灣
本書分類：電腦資訊> 程式設計/APP開發> 其他程式設計相關
```











# Search

https://search.books.com.tw/search/query/cat/all/key/Think%20Julia

# Ref:
1. https://github.com/Angela822
2. ISBN 找 books 的圖 https://youyouyou.pixnet.net/blog/post/118842408
3. 
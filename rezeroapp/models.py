from django.db import models

# 投稿内容
class RezeroPost(models.Model):

  # カテゴリーを3つタプルで
  CATEGORY = (("anything", "作品全体"),
              ("lastest", "最新話"),
              ("character", "キャラクター"))
  

  # カテゴリ
  category = models.CharField(
    verbose_name="カテゴリ",
    max_length=50,
    #　選択制
    choices=CATEGORY
  )

# タイトル
  title = models.CharField(
    verbose_name="タイトル",
    max_length=200
  )

  # 考察本文
  content = models.TextField(
    verbose_name="考察内容"
  )

  # 投稿日時
  posted_at = models.DateTimeField(
    verbose_name="投稿日時",
    # 自動追加
    auto_now_add=True
  )


# 管理サイト上でこのモデルを使ったデータを標示する際
# タイトルを表示させるのに必要
  def __str__(self):
    return self.title
  
# https://qiita.com/Yoshida-Programmer/items/7d021917b420743cb53f?utm_source=chatgpt.com
class Comment(models.Model):
    # 外部キーで考察の投稿と結ぶ
    # on_delete=models.CASCADEで親の投稿が消えた時にこのコメントも消える
    post = models.ForeignKey(RezeroPost, on_delete=models.CASCADE)
    text = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)
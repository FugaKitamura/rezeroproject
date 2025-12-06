from django import forms
from django.forms import ModelForm
from .models import RezeroPost
from .models import Comment

# お問い合わせのやつ
class ContactForm(forms.Form):
  name = forms.CharField(label="お名前")
  email = forms.EmailField(label="メールアドレス")
  message_title = forms.CharField(label="メッセージタイトル")
  message = forms.CharField(label="メッセージ")

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields["name"].widget.attrs["placeholder"] = \
      "お名前を入力"
    self.fields["name"].widget.attrs["class"] = "form-control"
    self.fields["email"].widget.attrs["placeholder"] = \
      "メールアドレスを入力"
    self.fields["email"].widget.attrs["class"] = "form-control"
    self.fields["message_title"].widget.attrs["placeholder"] = \
      "メッセージタイトルを入力"
    self.fields["message_title"].widget.attrs["class"] = "form-control"
    self.fields["message"].widget.attrs["placeholder"] = \
      "メッセージを入力"
    self.fields["message"].widget.attrs["class"] = "form-control"

# 投稿
class PostFrom(ModelForm):
  class Meta:
    model = RezeroPost
    fields = ["category", "title", "content"]
    widgets = {
            "title": forms.TextInput(attrs={"placeholder": "【〇〇話】タイトルを入力"}),
            }

# コメントのform
# たぶん上と同じでいいとおもう
class CommentForm(ModelForm):
  class Meta:
    model = Comment
    fields = ["text"]
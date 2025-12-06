from django.shortcuts import render

from django.views.generic import ListView, DetailView,FormView, TemplateView

from .models import RezeroPost,Comment
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import ContactForm,CommentForm
from django.contrib import messages
from django.core.mail import EmailMessage
from .forms import PostFrom
from django.shortcuts import redirect, get_object_or_404
from django import forms


# class作り
class IndexView(ListView):
  template_name = "index.html"
  context_object_name = "orderby_records"
  queryset = RezeroPost.objects.order_by("-posted_at")
  paginate_by = 10

class RezeroDetail(DetailView):
  template_name = "post_detail.html"
  model = RezeroPost
  # 参考　＞＞　https://qiita.com/Yoshida-Programmer/items/7d021917b420743cb53f?utm_source=chatgpt.com 
  # コメントの設定
  def get(self, request, *args, **kwargs):
    pk = kwargs.get("pk")

    # 投稿があるか
    if not RezeroPost.objects.filter(pk=pk).exists():
      return redirect("rezeroapp:index")

    return super().get(request, *args, **kwargs)

  # コメント機能
  def post(self, request, *args, **kwargs):
    self.object = self.get_object()
    text = request.POST.get('text', '').strip()
    if text:
      Comment.objects.create(post=self.object, text=text)
    context = self.get_context_data(object=self.object)
    return self.render_to_response(context)

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['post'] = self.object
    context['comments'] = self.object.comment_set.all().order_by('-posted_at')
    return context

class AnythingView(ListView):
  template_name = "anything_list.html"
  model = RezeroPost
  context_object_name = "anything_records"
  queryset = RezeroPost.objects.filter(category="anything").order_by("-posted_at")
  paginate_by = 3

class LastestView(ListView):
  template_name = "lastest_list.html"
  model = RezeroPost
  context_object_name = "lastest_records"
  queryset = RezeroPost.objects.filter(category="lastest").order_by("-posted_at")
  paginate_by = 3

class CharacterView(ListView):
  template_name = "character_list.html"
  model = RezeroPost
  context_object_name = "character_records"
  queryset = RezeroPost.objects.filter(category="character").order_by("-posted_at")
  paginate_by = 3

class ContactView(FormView):
  template_name = "contact.html"
  form_class = ContactForm
  success_url = reverse_lazy("rezeroapp:contact")
  def form_valid(self, form):
    name = form.cleaned_data["name"]
    email = form.cleaned_data["email"]
    message_title = form.cleaned_data["message_title"]
    message = form.cleaned_data["message"]
    subject = "お問い合わせ: {}".format(message_title)
    message = \
      "送信者名: {0}\nメールアドレス: {1}\n メッセージタイトル:{2}\n メッセージ:\n{3}".format(name,email,message_title,message)
    from_email = "ykh2538032@stu.o-hara.ac.jp"
    to_list = ["ykh2538032@stu.o-hara.ac.jp"]
    message = EmailMessage(subject=subject,
                           body=message,
                           from_email=from_email,
                           to=to_list,
                           )
    message.send()
    messages.success(
      self.request, "お問い合わせは正常に送信されました。")
    return super().form_valid(form)
  
# 投稿のためのviewのクラス
class PostView(CreateView):
  form_class = PostFrom
  template_name = "post.html"
  success_url = reverse_lazy("rezeroapp:post_done")

# 投稿した後のが目のクラス
class PostSuccessView(TemplateView):
  template_name = "post_success.html" 


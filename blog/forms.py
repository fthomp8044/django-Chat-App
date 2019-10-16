# from django import forms
# from blog.models import Chat, Comment
#
# class ChatForm(forms.ModelForm):
#
#     class Meta():
#         model = Chat
#         fields= ('author', 'title', 'text')
#
#         widgets = {
#             'title':forms.TextInput(atrrs={'class': 'textinputclass'}),
#             'text':forms.Textarea(attrs={'class': 'editable medium-editor-textarea chatcontent'})
#         }
#
# class CommentForm(forms.ModelForm):
#
#     class Meta():
#         model = Comment
#         fields = ('author', 'text')
# #use textinput widget with a class key which will go inside my css
#         widgets = {
#             'author':forms.TextInput(attrs={'class': 'textinputclass'}),
#             'text':forms.Textarea(attrs={'class': 'editable medium-editor-textarea chatcontent'})
#         }

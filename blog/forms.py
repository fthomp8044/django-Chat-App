from django import forms


# from parsley.decorators import parsleyfy
# @parsleyfy
class ChatForm(forms.ModelForm):

    class Meta():
        #target the Chat model class
        model = Chat
        #The fiels we want to go back and edit
        fields= ('name',)
#create a widget for customizations.
#first key will be the tile.
#textarea will have a large text area will a sub directory of 'class'.
#crated two classes. textinputclass and chatcontent
        widgets = {
            'name':forms.TextInput(atrrs={'class': 'textinputclass'}),
        }
# @parsleyfy
class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        #Whos writing the comment and can they go back and edit it
        fields = ('created_by', 'text')
#use textinput widget with a class key which will go inside my css
#keep the same styleing class as my textinputclass in the key title up top
# ---------medium-editor-textarea-------
        widgets = {
            'created_by':forms.TextInput(attrs={'class': 'textinputclass'}),
            'text':forms.Textarea(attrs={'class': 'editable'})
        }

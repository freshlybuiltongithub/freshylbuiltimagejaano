from numpy import array,argmax,expand_dims
from PIL import Image
from colorama import init,deinit,Fore
from pickle import load
from keras.models import load_model
from keras.applications.xception import Xception
from keras.preprocessing.sequence import pad_sequences
from .downloader import model_downloader

# Class image_description
class image_description:
	# Constructor of class
    def __init__(self,img_path,model_name):

        available_models={
            "img_desc":"model_29",
            "img_desc_r":"model_r_"
            }

        max_length = 32
        tokenizer = load(open("freshlybuiltimagejaano/tokenizer.p","rb"))
        if model_name in available_models:
            model_name=available_models[model_name]
            if model_downloader("img_desc").status_code==1000:
                model = load_model('freshlybuiltimagejaano/models/'+model_name+'.h5')
                xception_model = Xception(include_top=False, pooling="avg")
        init(autoreset=True)
        print(Fore.MAGENTA + self.generate_desc(model, tokenizer,self.extract_features(img_path, xception_model), max_length))
        deinit()
    # Function for Feature Extraction 
    def extract_features(self,filename, model):
        image = Image.open(filename)
        image = image.resize((299,299))
        image = array(image)
        # converting 4 channel image to 3 channel
        if image.shape[2] == 4: 
            image = image[..., :3]
        image = expand_dims(image, axis=0)
        image = image/127.5
        image = image - 1.0
        feature = model.predict(image)
        return feature
    # Function for Retrieving Words by index value from tokenizer file
    def word_for_id(self,integer, tokenizer):
        for word, index in tokenizer.word_index.items():
            if index == integer:
                return word
        return None
    # Function for Generate Descriptions 
    def generate_desc(self,model, tokenizer, photo, max_length):
        in_text = 'start'
        for i in range(max_length):
            sequence = tokenizer.texts_to_sequences([in_text])[0]
            sequence = pad_sequences([sequence], maxlen=max_length)
            pred = model.predict([photo,sequence], verbose=0)
            pred = argmax(pred)
            word = self.word_for_id(pred, tokenizer)
            if word is None:
                break
            in_text += ' ' + word
            if word == 'end':
                break
        return in_text

"""debugger"""
#image_name=input('image_name: ')
#image_description(image_name)

# Docker_NLP
Project for testing Spacy for NLP and Tensorflow for Image Classification in a Docker container with restful API access
## Usage
To access you need to register a user, using curl or any software like postman into server_url:5000:

 - Welcome, '/'
 - Register, '/register' : expects a json with a 'user' and a 'password', returns the positive or negative outcome of the transaction;
 - Login, '/login' : expects a json with a 'user' and a 'password', returns the positive or negative outcome of the transaction;;
 - Update_Pw, '/update_pw' : expects a json with a 'user', a 'old_password' and a 'new_password', returns the respective outcome;
 
 ##NLP
 - Score_Nlp_Strings, '/score_strings' : expects a 'user', a 'password', a 'original_text' and 'new_text' in english, returns the ratio of similarity.
 - Score_Nlp_Text_Urls, '/score_urls' : expects a 'user', a 'password', a 'url_1' and 'url_2' from pages in english, returns the ratio of similarity between the text in it.
 
 ##Tensorflow Classification
 - Classify_Image, 'classify_image' : expects a 'user', a 'password', a 'image_url', returns a possible classification.
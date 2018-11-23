def get_info(id):
  id = str(id)
  if id.isdigit():
    mas = api.users.get(user_ids=id, fields= 'online, last_seen, bdate, counters, domain, country, city')
    with open('users_info.txt', 'a') as f:
       a, b = id, str("{0:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now()))
       f.write(f'==== Получение информации о пользователе с id = {a} | дата-время:{b} === \n')
       json.dump({"user_info": mas}, f, indent=4, ensure_ascii=False)
       f.write('\n')
  else:
    print('id пользователя состоит только из цифр!')

def get_type_and_id(name):
  with open('get_type_and_id.txt', 'a') as f:
       a = name
       b = str("{0:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now()))
       f.write(f'==== Определение id и type по username = {a} | дата-время:{b} === \n')
       result = api.utils.resolveScreenName(screen_name=name)
       json.dump(result, f, indent=4, ensure_ascii=False)
       f.write('\n')
 
def send_message(id):
  with open('message_text.txt', 'r') as f:
    text = ''
    for line in f:
      text+=line
  api.messages.send(user_id=str(id), message=text, attachment = 'photo208608238_456242857')
  print("Сообщение отправлено!")

def messages_history(id,number):
  history = api.messages.getHistory(count=number, user_id=str(id), start_message_id = -1)
  with open('history.txt', 'a') as f:
       a,b = str(number),str(id)
       c = str("{0:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now()))
       f.write(f'Получения последних {a} сообщений диалога с пользователем с id = {b} | дата-время:{c} \n')
       json.dump(history, f, indent=4, ensure_ascii=False)
       f.write('\n')
 
def get_photo_likes(id_owner, id_item):
  likes = api.likes.getList(type='photo', owner_id=str(id_owner), item_id=str(id_item))
  with open('likes.txt', 'a') as f:
     a,b = str(id_owner),str(id_item)
     c = str("{0:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now()))
     f.write(f'Кол-во лайков фотографии с id = {b} пользователя с id = {a} + список id-лайкнувших | дата-время:{c} \n')
     json.dump(likes, f, indent=4, ensure_ascii=False)
     f.write('\n')

if __name__ == "__main__":
  import vk, json, re, datetime
  pattern = r'[^\.a-z0-9]'
  token = "YOUR TOKEN"
  if re.search(pattern, token):
    print('Invalid token!')
  else:
    session = vk.AuthSession(access_token= token)
    api = vk.API(session, v='5.35', lang='en', timeout=10)

   #et_info(208608238)
   #get_type_and_id('skorking')
   #send_message(208608238)
   #messages_history(208608238,3)
   #get_photo_likes(34045589, 456251564)


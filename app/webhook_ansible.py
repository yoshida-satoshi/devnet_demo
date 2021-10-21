
import message

from flask import Flask, request
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def stop_mailmagazine():

    user_message = message.get_message(request) 

    print(f'message is: {user_message}')

    if user_message == 'who are you?':
        message.send_message('私ハ botデス')

    if user_message == 'how are you?':
        message.send_message('I feel like a robot.')

    if user_message == 'Melden Sie sich von unserem Newsletter ab.':
        pass
    
    return 'Complete!', 200



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80, threaded=True)
    
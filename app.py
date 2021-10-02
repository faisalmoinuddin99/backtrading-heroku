from flask import Flask, render_template, request
from datetime import datetime
import backtrader as bt
from strategies import TestStrategy
from strategies import SmaCross


app = Flask(__name__)



'''@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # print(request.form) ImmutableMultiDict([('youtube_link', 'https://youtu.be/jWtztbHctl4')])
        myDict = request.form
        print(myDict)
        yt_link = myDict['youtube_link']  # url
        disk_link = myDict['disk_link']

        try:
            yt = YouTube(yt_link, on_progress_callback=on_progress)
            video_title = yt.title
            print("Title " + video_title)

            SAVE_PATH = disk_link
            # data = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(SAVE_PATH)
            # .download(SAVE_PATH)
            stream = yt.streams.first()
            stream.download(SAVE_PATH)

        except Exception as error:
            error_string = repr(error)
            return render_template('show.html', error_string=error_string)

        return render_template('show.html', video_title=video_title)

    return render_template('index.html')
'''

@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # print(request.form) ImmutableMultiDict([('youtube_link', 'https://youtu.be/jWtztbHctl4')])
        print(request.form)
        myDict = request.form
        print(myDict)
        setCash = myDict['setCash']  # url
        try:
            convertedCash = float(setCash)
        except Exception as error:
            error_string = repr(error)
            return render_template('show.html', error_string=error_string)

        selectedStrategy = myDict['strategy_type']
        print(setCash, selectedStrategy)
        print(type(float(setCash)))
        print(type(selectedStrategy))
        strategy = selectedStrategy


        print(strategy)
        try:
            cerebro = bt.Cerebro()
            cerebro.broker.setcash(convertedCash)
            if (strategy == 'TestStrategy'):
                cerebro.addstrategy(TestStrategy)

                data = bt.feeds.YahooFinanceData(dataname="INFY.csv", fromdate=datetime(2015, 1, 1),
                                         todate=datetime(2021, 1, 1))
                print('data',data)
                cerebro.adddata(data)
                print('run',cerebro.run())
                cerebro.plot()
            else:
                cerebro.addstrategy(SmaCross)
                data = bt.feeds.YahooFinanceData(dataname="INFY.csv", fromdate=datetime(2015, 1, 1),
                                             todate=datetime(2021, 1, 1))
                print('data', data)
                cerebro.adddata(data)
                print('run', cerebro.run())
                cerebro.plot()
        except Exception as error:
            error_string = repr(error)
            return render_template('show.html', error_string=error_string)

        return render_template('index.html')
    return render_template('index.html')


@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True, port=8000)
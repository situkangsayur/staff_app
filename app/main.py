from . import create_app

# panggil create_app lalu mendapatkan return value berupak flask app
app = create_app('development')

if __name__ == '__main__':
    # jalan kan flask app
    app.run('0.0.0.0')

# -*- coding: utf-8 -*-
import os
from module.initial import create_app

app = create_app(os.getenv('FLASK_CONFIG') or 'default')


# shell注入
@app.shell_context_processor
def make_shell_context():
    return dict(app=app)


if __name__ == '__main__':
    app.run(debug=True)

from app import app
from flask import render_template, redirect, url_for, request
import random

@app.route('/', methods=['GET'])
def index() :
    if request.method == 'GET' :
        return render_template('index.html')

@app.route('/choose', methods=['POST'])
def choose() :
    result = request.form

    # create candidate menus
    menus = [
        "손가네칼국수", "마피아떡볶이", "해피덮", "빨강파이프", "고래심줄",
        "미소야", "알촌", "밥이라면", "홍춘", "산골막창", "브라더양식당",
        "쭈꾸미와삼겹살", "선영이네", "고수찜닭", "내가찜한닭"
    ]
    if 'package_included' in result :
        menus.extend(['노브랜드 버거', '한솥', '에그드랍', 'KFC', '서브웨이'])
            
    # choose one
    choice = random.choice(menus)
    print(choice)
    return redirect(url_for('index'))
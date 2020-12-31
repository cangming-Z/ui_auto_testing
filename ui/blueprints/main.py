from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)


@main_bp.route('/main')
def main():
    return render_template('测试ajax.html')

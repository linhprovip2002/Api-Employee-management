#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AppServer.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
# """Django's command-line utility for administrative tasks."""
# import os
# import sys

# def main():
#     """Run administrative tasks."""
#     os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AppServer.settings')
#     try:
#         from django.core.management import execute_from_command_line
#     except ImportError as exc:
#         raise ImportError(
#             "Couldn't import Django. Are you sure it's installed and "
#             "available on your PYTHONPATH environment variable? Did you "
#             "forget to activate a virtual environment?"
#         ) from exc
    
#     # Đặt giá trị cổng trực tiếp trong đoạn mã
#     port = 9000
#     # Đọc giá trị cổng từ biến môi trường
#     # port = int(os.environ.get("PORT", 8000))

#     # Thêm giá trị cổng vào danh sách đối số để chạy lệnh runserver
#     execute_from_command_line([sys.argv[0], 'runserver', f'192.168.43.253:{port}'])

# if __name__ == '__main__':
#     main()

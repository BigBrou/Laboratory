from datetime import datetime

hour = datetime.now().hour
afternoon = 12;

if hour > afternoon:
    print('afternoon')
elif hour < afternoon:
    print('morning')
else:
    print('O\'Clock')

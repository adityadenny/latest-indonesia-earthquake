import requests
from bs4 import BeautifulSoup


def data_extraction():
    """
    Below is example data want to show:
    Date : 03 Maret 2022,
    Time : 13:37:04 WIB
    Magnitude : 4.8
    Depth : 10 km
    Location : 0.15 LU - 100.00 BT
    Epicenter : Pusat gempa berada di darat 8 km tenggara Talu
    Feel : Dirasakan (Skala MMI): III Pasaman Barat, I-II Padang Panjang, I-II Pariaman
    :return:
    """
    try:
        content = requests.get('https://www.bmkg.go.id/')
    except Exception:
        return None

    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')
        datetime = soup.find('span', {'class': 'waktu'})
        datetime = datetime.text.split(', ')
        date = datetime[0]
        time = datetime[1]

        items = soup.find('div', {'class': "col-md-6 col-xs-6 gempabumi-detail no-padding"})
        items = items.findChildren('li')
        i = 0
        magnitudo = None
        ls = None
        bt = None
        depth = None
        location = None
        feel = None

        for res in items:
            # print(i, res)
            if i == 1:
                magnitudo = res.text
            elif i == 2:
                depth = res.text
            elif i == 3:
                coordinate = res.text.split(' - ')
                ls = coordinate[0]
                bt = coordinate[1]
            elif i == 4:
                location = res.text
            elif i == 5:
                feel = res.text

            i = i + 1

        results = dict()
        results['date'] = date  # '03 Maret 2022'
        results['time'] = time  # '13:37:04 WIB'
        results['magnitude'] = magnitudo  # 4.8
        results['koordinate'] = [ls, bt]  # {'LU': 1.48, 'BT': 100.00}
        results['depth'] = depth  # '10 km'
        results['location'] = location  # {'LU': 1.48, 'BT': 100.00}
        # results['epicenter'] = 'Pusat gempa berada di darat 8 km tenggara Talu'
        results['feel'] = feel  # 'Dirasakan (Skala MMI): III Pasaman Barat, I-II Padang Panjang, I-II Pariaman'
        return results
    else:
        return None


def show_data(result):
    if result is None:
        print("Tidak bisa menemukan data gempa terkini")
        return
    print('Latest Earthquake based on bmkg.go.id:')
    print(f"Date : {result['date']}")
    print(f"Time : {result['time']}")
    print(f"Magnitude : {result['magnitude']}")
    print(f"Coordinate : {result['koordinate'][0]}, {result['koordinate'][1]}")
    print(f"Depth : {result['depth']}")
    print(f"Location : {result['location']}")
    # print(f"Epicenter : {result['epicenter']}")
    print(f"Feel : {result['feel']}")


if __name__ == '__main__':
    result = data_extraction()
    show_data(result)

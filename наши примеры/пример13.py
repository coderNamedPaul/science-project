l1 = ['P', 'A', 'R']
l2 = ['Paul', 'Ann', 'Rodion']
dct2 = dict.fromkeys(l1, l2)  # ������ ������ , ����� ����� ����, � ���������� ������
print(dct2)
dct2['P'] = 'Paul'
dct2['R'] = 'Rodion'
dct2['A'] = 'Ann'
print(dct2)  # ������ ��� ��� ��� � �����

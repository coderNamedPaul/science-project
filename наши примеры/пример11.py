l1 = [1, 2, 4, 3, 5, 4, 3, 6, 1, 2, 8, 7, 9]
l2 = ['Ann', 'Paul', 'Rodion', 'Max', 'Matt', 'Billy', 'Thomas']
print(l2.index('Paul'))
print(l1.index(2, 4))  # ���� ������ ������ �� ������� � ���������� ������
print(l1.count(3))
l1.sort()
print(l1)
l2.sort(reverse=True)  # � �������� �������
l2.append('Tom')
print(l2)
l1.remove(1)
print(l1)
name0 = l2.pop(0)
print(l2)
print(name0)
l1.extend([1, 2])
print(l1)
l1.insert(0, l2)  # �� �������� ��������� ������
print(l1)
print(l1[0][3])  # ����� ������� � ��������� � ���������� ������ � ������ �� ��� ��������� � ��� ��� �������� 3

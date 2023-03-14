import operation as op


def functional(choice):
    if choice == 1:
        op.add()
    if choice == 2:
        op.show('all')
        op.id_edit_del_show('edit')
    if choice == 3:
        op.show('all')
    if choice == 4:
        op.show('date')
    if choice == 5:
        op.show('id')
        op.id_edit_del_show('show')
    if choice == 6:
        op.show('all')
        op.id_edit_del_show('del')



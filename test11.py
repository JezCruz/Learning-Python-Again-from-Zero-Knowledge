# Add names to a variable and create an input function that searches for a name in the list.


names = ['jezreel','james','migs','ruru','kokoy','angel']


x = input('search names: ')


if x in names:
    print('name: \''+ x +'\' found.')

    # output:

    # search names: jezreel
    # name: 'jezreel' found.

else:
    print('no \''+ x +'\' name on the list.')

    # output:

    # search names: nana
    # no 'nana' name on the list.
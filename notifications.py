from win10toast import ToastNotifier

# checkt hoeveel capaciteit in gebruik is
def check_capaciteit(container):
    # als de container 80 procent capaciteit of hoger heeft stuur een notificatie.
    if container >= 80:
        toaster = ToastNotifier()
        toaster.show_toast("Container bijna vol", "Container moet geleegd worden")


check_capaciteit(80)

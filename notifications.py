from win10toast import ToastNotifier

def check_capaciteit(container):
    if container >= 80:
        toaster = ToastNotifier()
        toaster.show_toast("Container bijna vol", "Container moet geleegd worden")


check_capaciteit(80)

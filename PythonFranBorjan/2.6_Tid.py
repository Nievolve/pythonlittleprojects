
def convert_to_hms(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = (seconds % 3600) % 60
    return hours, minutes, seconds

def main():
    seconds = int(input("Ange antal sekunder: "))
    hours, minutes, seconds = convert_to_hms(seconds)
    print(f"Tid: {hours} timmar, {minutes} minuter, {seconds} sekunder.")

main()

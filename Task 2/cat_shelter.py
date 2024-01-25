import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Missing Command line arugment")
        sys.exit(1)
    else:
        # The first argument (index 0) is the script name, so the file path is at index 1
        file_path = sys.argv[1]

        try:
            with open(file_path, 'r') as file:
               # Process the file contents here
                lines = file.readlines()

                cat_visits = 0
                other_cats = 0
                total_time_in_house = 0
                durations = []

                for line in lines:
                    if line.strip() == 'END':
                        break

                    data = line.strip().split(',')

                    if len(data) != 3:
                        print(f"Invalid log entry: {line}")
                        continue

                    cat_name, entry_time, exit_time = data

                    try:
                        entry_time = int(entry_time)
                        exit_time = int(exit_time)
                    except ValueError:
                        print(f"Invalid time format in log entry: {line}")
                        continue

                    if cat_name == 'OURS':
                        cat_visits += 1
                        total_time_in_house += exit_time - entry_time
                        durations.append(exit_time - entry_time)
                    else:
                        other_cats += 1

                if cat_visits == 0:
                    print("No cat visits found in the log.")
                else:
                    average_duration = sum(durations) / cat_visits
                    longest_duration = max(durations)
                    shortest_duration = min(durations)

                    print("\nLog File Analysis\n==================\n")
                    print(f"Cat Visits in house: {cat_visits}")
                    print(f"Other Cats: {other_cats}")
                    print("\nTotal Time in House: {} Hours, {} Minutes".format(total_time_in_house // 60, total_time_in_house % 60))

                    # For the correct cat only
                    print("\nAverage Visit Length for correct cat: {:.2f} Minutes".format(average_duration))
                    print("Longest Visit length for correct cat: {} Minutes".format(longest_duration))
                    print("Shortest Visit length for correct cat: {} Minutes".format(shortest_duration))

        except FileNotFoundError:
            print(f"Cannot: open - {file_path}")
        except Exception as e:
            print(f"Error: {e}")
        

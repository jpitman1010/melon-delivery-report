# melon-delivery-report
def melon_count(day_count,path):
    """The produce report for each day are produced

    for each_line in delivery_report:
    by opening each report, looking at each line in the report
    and giving an outcome for each report"""
    delivery_report=open(path)
    print("Day",day_count)

    for line in delivery_report:
        line=line.rstrip()
        # remove the white spaces from each line
        words=line.split("|")
        # take each line and break it into a list of words/strings separated by | in original strings.
        melon = words[0]
        # first word in string 
        count = words[1]
        # second word in string
        amount = words[2]
        # third word in string

        print("Delivered {} {}s for total of ${}".format(count,melon,amount))
        # print statement for each line.
    delivery_report.close()
    # close the delivery report before opening the next when next fcn is called.

melon_count(1, "um-deliveries-20140519.txt")
melon_count(2, "um-deliveries-20140520.txt")
melon_count(3, "um-deliveries-20140521.txt")
# call the fnc 3 diff times for each file.

    # print("Day 1")
    # the_file = open("um-deliveries-20140519.txt")
    # for line in the_file:
    #     line = line.rstrip()
    #     words = line.split('|')

    #     melon = words[0]
    #     count = words[0]
    #     amount = words[0]

    #     print("Delivered {} {}s for total of ${}".format(
    #         count, melon, amount))
    # the_file.close()


    # print("Day 2")
    # the_file = open("um-deliveries-20140520.txt")
    # for line in the_file:
    #     line = line.rstrip()
    #     words = line.split('|')

    #     melon = words[0]
    #     count = words[0]
    #     amount = words[0]

    #     print("Delivered {} {}s for total of ${}".format(
    #         count, melon, amount))
    # the_file.close()


    # print("Day 3")
    # the_file = open("um-deliveries-20140521.txt")
    # for line in the_file:
    #     line = line.rstrip()
    #     words = line.split('|')

    #     melon = words[0]
    #     count = words[0]
    #     amount = words[0]

    #     print("Delivered {} {}s for total of ${}".format(
    #         count, melon, amount))
    # the_file.close()

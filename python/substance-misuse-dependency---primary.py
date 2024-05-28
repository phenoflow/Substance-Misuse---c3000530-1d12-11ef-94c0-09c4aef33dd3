# Kathryn M Abel, Holly Hope, Eleanor Swift, Rosa Parisi, Darren M Ashcroft, Kyriaki Kosidov, Semre Su Osam, Christian Dolman, Mathias Pierce, 2024.

import sys, csv, re

codes = [{"code":"E242.00","system":"readv2"},{"code":"E245.12","system":"readv2"},{"code":"E246000","system":"readv2"},{"code":"E247200","system":"readv2"},{"code":"E248100","system":"readv2"},{"code":"E240.00","system":"readv2"},{"code":"Eu16200","system":"readv2"},{"code":"E248z00","system":"readv2"},{"code":"E249z00","system":"readv2"},{"code":"E245100","system":"readv2"},{"code":"E245.11","system":"readv2"},{"code":"E246100","system":"readv2"},{"code":"E240.14","system":"readv2"},{"code":"E249000","system":"readv2"},{"code":"E248000","system":"readv2"},{"code":"E247z00","system":"readv2"},{"code":"E240100","system":"readv2"},{"code":"E240.12","system":"readv2"},{"code":"Eu11200","system":"readv2"},{"code":"E248.00","system":"readv2"},{"code":"Eu14200","system":"readv2"},{"code":"8HHL.00","system":"readv2"},{"code":"1463.00","system":"readv2"},{"code":"E241.13","system":"readv2"},{"code":"E243300","system":"readv2"},{"code":"L183.11","system":"readv2"},{"code":"E240000","system":"readv2"},{"code":"E243100","system":"readv2"},{"code":"E240.11","system":"readv2"},{"code":"8B23.13","system":"readv2"},{"code":"E24..00","system":"readv2"},{"code":"E249100","system":"readv2"},{"code":"Eu12200","system":"readv2"},{"code":"E245200","system":"readv2"},{"code":"E243.11","system":"readv2"},{"code":"E243200","system":"readv2"},{"code":"E245z00","system":"readv2"},{"code":"E240200","system":"readv2"},{"code":"E249.00","system":"readv2"},{"code":"8BAX.00","system":"readv2"},{"code":"Eu1A200","system":"readv2"},{"code":"E243000","system":"readv2"},{"code":"E242z00","system":"readv2"},{"code":"E246.00","system":"readv2"},{"code":"1283.00","system":"readv2"},{"code":"E242100","system":"readv2"},{"code":"E24z.00","system":"readv2"},{"code":"E240z00","system":"readv2"},{"code":"E249200","system":"readv2"},{"code":"E245.00","system":"readv2"},{"code":"8BAW.00","system":"readv2"},{"code":"Z192.00","system":"readv2"},{"code":"E247.00","system":"readv2"},{"code":"E243z00","system":"readv2"},{"code":"E248200","system":"readv2"},{"code":"E246200","system":"readv2"},{"code":"E243.00","system":"readv2"},{"code":"8I2N.00","system":"readv2"},{"code":"E247000","system":"readv2"},{"code":"E243.13","system":"readv2"},{"code":"E242200","system":"readv2"},{"code":"E242000","system":"readv2"},{"code":"E247100","system":"readv2"},{"code":"E245000","system":"readv2"},{"code":"E246z00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('substance-misuse-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["substance-misuse-dependency---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["substance-misuse-dependency---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["substance-misuse-dependency---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)

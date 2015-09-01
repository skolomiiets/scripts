import shutil, time, sys
try:
    sys.argv[1], sys.argv[2]
except:
    sys.exit("Use of this script: " + sys.argv[0] + " pathofzip pathtolocationzip")
data = time.strftime("%d%m-%H_%M")
ziparch = '%s_%s' % (sys.argv[2], data)
shutil.make_archive(ziparch, 'zip', sys.argv[1])

new_name = "MACROPAD2"
import storage
storage.remount("/", readonly=True)
m = storage.getmount("/")
m.label = new_name
storage.remount("/", readonly=True)
import sys, platform, pkg_resources

print("Python:", sys.version)
print("Platform:", platform.platform())
print("Installed packages:")
for dist in pkg_resources.working_set:
    print(f"{dist.key}=={dist.version}")

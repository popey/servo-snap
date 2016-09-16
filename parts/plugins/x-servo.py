
import os
import shutil
import subprocess
import snapcraft

class ServoBuildPlugin(snapcraft.BasePlugin):

    @classmethod
    def schema(cls):
        schema = super().schema()
        schema['properties']['configflags'] = {
            'type': 'array',
            'minitems': 1,
            'uniqueItems': True,
            'items': {
                'type': 'string',
            },
            'default': [],
        }

        # Inform Snapcraft of the properties associated with building. If these
        # change in the YAML Snapcraft will consider the build step dirty.
        schema['build-properties'].append('configflags')

        return schema

    def __init__(self, name, options, project):
        super().__init__(name, options, project)
        self.build_packages.extend(['make'])

    def build(self):
        super().build()

        env = self._build_environment()
        print(env)
        # This builds servo
        self.run(['./mach', 'build', '--release'], env=env)

        # This makes a tarball, which we're doing because upstream currently
        # doesn't have an 'install' option which copies files, so we make the
        # tarball then unpack it into the target
        self.run(['./mach', 'package'], env=env)
        print(env)
        cwd=subprocess.check_output('pwd').decode("utf8").replace('\n', ' ')
        # Unpack tarball into install dir
        self.run(['ls', '-l', 'target'], env=env)
        self.run(['cp', '-av', 'target/release/', self.installdir+'/servo'], env=env)
#        self.run(['tar', 'zxvf', 'target/*.tar.gz', '-C', self.installdir], env=env)


    def _build_environment(self):
        env = os.environ.copy()
        # Try to set rust compiler to multi-threads as per:-
        # https://internals.rust-lang.org/t/default-settings-for-parallel-codegen/519
        env['codegen-units'] = '4'
        return env

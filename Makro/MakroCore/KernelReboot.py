from Makro.MakroCore import flags
import importlib
import pkgutil
import sys


class KernelReboot:
    """
    Reloads all modules in the MakroCore/ directory while preserving runtime session state.
    This includes logged-in user, terminal mode, and any other live context in flags.py.
    """

    def __init__(self):
        self.package = 'MakroCore'
        self.MakroCore_path = f'{flags.base_folder}/{self.package}'
        self.exclude = {'MakroCoreReloader', '__init__'}
        self.modules = self._find_modules()

    def _find_modules(self):
        """Discover reloadable modules inside MakroCore/."""
        return {
            name for _, name, _ in pkgutil.iter_modules([self.MakroCore_path])
            if name not in self.exclude
        }

    def reload_all(self):
        """Reload all MakroCore modules and restore important runtime state."""
        try:
            # 1. Backup persistent state from flags.py
            persistent = {
                'USERNAME': flags.USERNAME,
                'PASSWORD': flags.PASSWORD,
                'MODE': flags.MODE,
                'FTU': flags.FTU,
                'EnableIntSoft': flags.EnableIntSoft,
                'EnableGUI': flags.EnableGUI,
                'EnableAudio': flags.EnableAudio,
                
                'UserLess_Connection': flags.UserLess_Connection,
                'Run_Threads_Inside': flags.Inside_Thread,
                'Run_Straight_Builtin': flags.Run_Straight_Builtin,
                'GO_TO_FTU': flags.GO_TO_FTU,
                'Fully_GUI': flags.Fully_GUI,
                'Create_Graph': flags.Create_Graph,
                'Runtime_Tracer': flags.Runtime_Tracer,
                
                'pl': flags.pl,
                'sys_detect': flags.sys_detect,
                'base_folder': flags.base_folder,
                'Module': flags.Module,
                'LCommand': flags.LCommand,
                
                # Add other variables you want to preserve here
            }

            # 2. Reload modules
            for mod in self.modules:
                full_name = f"{self.package}.{mod}"
                if full_name in sys.modules:
                    importlib.reload(sys.modules[full_name])
                else:
                    importlib.import_module(full_name)

            # 3. Restore state
            for key, value in persistent.items():
                setattr(flags, key, value)

            return True

        except Exception as e:
            print(f"[MakroCoreReloader] Reload failed: {e}")
            return False
#!/usr/bin/python
EXAMPLES = '''
- name: yum -q updateinfo security
  yum_patchlist:
    name: updateinfo
    show: security
'''
from ansible.module_utils.basic import AnsibleModule, load_platform_subclass
run_cmd = 'yum'

def _list_security_updateinfo(module):
#    yum updateinfo list security all
    cmd = "%s '%s' '%s' '%s' '%s'" % (run_cmd, 'updateinfo', 'list', 'security', 'all')
    rc, out, err = module.run_command(cmd, encoding=None)
    if rc is 0:
      result = { 'stdout':out, 'stderr':err, 'rc':rc, 'changed':True }
    else:
      result = { 'stdout':out, 'stderr':err, 'rc':rc, 'changed':False }    
    module.exit_json(**result)

def main():   
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(type='str', required=True),
            show=dict(type='str'),
        ),
        supports_check_mode=True,
    )
    
    name = module.params['name']
    show = module.params['show']
    if name == 'updateinfo':
        _list_security_updateinfo(module)

if __name__ == '__main__':
    main()

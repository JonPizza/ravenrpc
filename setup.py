from distutils.core import setup
setup(
  name = 'ravenrpc',         
  packages = ['ravenrpc'],   
  version = '0.1',      
  license='MIT',     
  description = 'Crazy simple Ravencoin RPC library',
  author = 'JonPizza',
  author_email = 'jon@jon.network',
  url = 'https://jon.network',
  download_url = 'https://github.com/JonPizza/ravenrpc/archive/v_01.tar.gz',
  keywords = ['Ravencoin', 'RPC'], 
  install_requires=[
          'requests'
      ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)

from setuptools import setup

setup(name='cufflinks',
      version='0.7.4',
      description='Productivity Tools for Plotly + Pandas',
      author='Jorge Santos',
      author_email='santos.jorge@gmail.com',
      license='MIT',
      keywords = ['pandas', 'plotly', 'plotting'],
      url = 'https://github.com/santosjorge/cufflinks',
      packages=['cufflinks'],
      install_requires = ['pandas','plotly>=1.7.6','colorlover>=0.2'],
	  zip_safe=False)

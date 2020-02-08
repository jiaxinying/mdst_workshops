import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as ss

fig=plt.figure()
ax1=fig.add_subplot(311)
x=np.linspace(0,10,100)
ax1.plot(x,np.cos(x))
ax2=fig.add_subplot(312)
ax2.plot(x,np.cos(x+1))
ax3=fig.add_subplot(313)
ax3.plot(x,np.cos(x+2))
ax=[ax1,ax2,ax3]
names=['signal 1','signal 2','signal 3']
i=0
for t in ax:
    t.set(xticks=[])
    t.set(yticks=[])
    t.set(title=names[i])
    i+=1
plt.show()
filepath_hospital=r'./HospitalAdmissionsData.csv'
hospital=pd.read_csv(filepath_hospital)
print('a----------')
print(hospital.columns)
print('b----------')
print(hospital.info())
print('1 festure is float, 4 features are integers')
print('c----------')
print('Admission_Type, Insurance_Type,Religion_Type,Race,Dx are objects')
print('d---------')
print(hospital.Insurance_Type.unique())
print('e-----------')
print(hospital.AdmissionLengthDays.describe())
print('f-----------')
print(hospital.describe(include='object'))
print('see top')

hospital.hist(column='AdmissionLengthDays')
plt.title("Histogram for Admissian Day")
plt.xlabel("AdmissionLengthDays")
plt.show()

hospital.hist(column='AdmissionLengthDays',log=True)
plt.title("Histogram for Admissian Day")
plt.xlabel("AdmissionLengthDays")
plt.show()

#hospital.boxplot(column='AdmissionLengthDays', by='Death_1')
#plt.suptitle('')
#plt.title('Boxplot of AdmissionLengthDays by whether survive')
#plt.xlabel('Died(1 = Yes)')
#plt.ylabel('AdmissionLengthDays')
#plt.tight_layout()
#plt.show()

bar=hospital.groupby('Death_1').mean()
bar.plot.bar(y=['AdmissionLengthDays'])
plt.title('Average AdmissionLengthDays for whether died')
plt.ylabel('Average length of admission')
plt.xlabel('IfDied (1 = Died)')
plt.show()
print('i-----------')
print(pd.crosstab(hospital.Death_1,hospital.Insurance_Type))
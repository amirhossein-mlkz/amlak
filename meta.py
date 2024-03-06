from uiFiles.main_UI import Ui_MainWindow

class Form:

    def __init__(self, ui:Ui_MainWindow) -> None:
        self.ui = ui
        
        self.melk_post_type = {
            'melk-status': {
                'type': 'select',
                'options' : 'melk-status',
            },

        'melk-category' : {
                'input': self.ui.melkCategoryFormInpt,
                'label': self.ui.melkCategoryFormLbl,
                'error': self.ui.melkCategoryFormError,

                'type': 'select',
                'options' : 'melk-category',
            },

        'city' : {
                'input':self.ui.cityFormInpt,
                'label':self.ui.cityFormLbl,
                'type': 'text',
            },

        'region' : {
            'input':self.ui.regionFormInpt,
            'label':self.ui.regionFormLbl,
            'type': 'number',
        },

        'street' : {
            'input':self.ui.streetFormInpt,
            'label':self.ui.streetFormLbl,
            'type': 'text',
        },

        'address' : {
            'input':self.ui.addressFormInpt,
            'label':self.ui.addressFormLbl,
            'type': 'textarea',
        },

        'owner-name1' : {
            'input':self.ui.ownerName1FormInpt,
            'label':self.ui.ownerName1FormLbl,
            'type': 'text',
        },

        'owner-name2' : {
            'input':self.ui.ownerName2FormInpt,
            'label':self.ui.ownerName2FormLbl,
            'type': 'text',
        },

        'owner1-mobile-number' : {
            'input':self.ui.owner1MobileNumberFormInpt,
            'label':self.ui.owner1MobileNumberFormLbl,
            'type': 'text',
        },

        'owner2-mobile-number' : {
            'input':self.ui.owner2MobileNumberFormInpt,
            'label':self.ui.owner2MobileNumberFormLbl,
            'type': 'text',
        },
        
        'owner1-phone-number' : {
            'input':self.ui.owner1PhoneNumberFormInpt,
            'label':self.ui.owner1PhoneNumberFormLbl,
            'type': 'text',
        },

        'tenant_name' : {
            'input':self.ui.tenantNameFormInpt,
            'label':self.ui.tenantNameFormLbl,
            'type': 'text',
        },

        'tenant-phone-number' : {
            'input':self.ui.tenantPhoneNumberFormInpt,
            'label':self.ui.tenantPhoneNumberFormLbl,
            'type': 'text',
        },

        'guard-name' : {
            'input':self.ui.guardNameFormInpt,
            'label':self.ui.guardNameFormLbl,
            'type': 'text',
        },
        
        'guard-phone-number' : {
            'input':self.ui.guardPhoneNumberFormInpt,
            'label':self.ui.guardPhoneNumberFormLbl,
            'type': 'text',
        },

        'owner-description':{
            'input':self.ui.ownerDescriptionFormInpt,
            'label':self.ui.ownerDescriptionFormLbl,
            'type': 'text',
        },


        'compensation' : {
            'title':'معاوضه',
            'type': 'radio',
            'options' : 'yes',  
        },

        'compensation-condition' : {
            'title':'شرایط معاوضه',
            'type': 'radio',
            'options' : 'yes',  
        },

        'participation' : {
            'title':'مشارکت',
            'type': 'radio',
            'options' : 'yes',
        },

        'document-status' : {
            'title':'وضعیت سند',
            'type': 'select',
            'options' : 'document-status',
            },

        'meterage' : {
            'title':'متراژ',
            'type': 'number',
        },

        'building-meterage' : {
            'title':'متراژ ساخت',
            'type': 'number',
        },

        'land-meterage' : {
            'title':'متراژ زمین',
            'type': 'number',
        },

        'length' : {
            'title':'طول',
            'type': 'number',
        },

        'width' : {
            'title':'َعرض',
            'type': 'number',
        },

        'opening-width'  : {
            'title':'عرض دهانه',
            'type': 'number',
        },
        
        'total-price'  : {
            'title':'قیمت کل',
            'type': 'number',
        },

        'unit-price'  : {
            'title':'قیمت هر متر مربع',
            'type': 'number',
        },

        'mortgage-price' : {
            'title':'قیمت رهن',
            'type': 'number',
        },

        'rent-price' : {
            'title':'قیمت اجاره',
            'type': 'number',
        },

        'construction-year' : {
            'title':'سال ساخت',
            'type': 'number',
        },

        'floor' : {
            'title':'طبقه',
            'type': 'number',
        },

        'floor-count' : {
            'title':'تعداد طبقات',
            'type': 'number',
        },

        'total-building-unit' : {
            'title':'تعداد کل واحدها',
            'type': 'number',
        },
        
        'floor-unit-count' : {
            'title':'تعداد واحد در طبقه',
            'type': 'number',
        },

        'floors-overal-info' : {
            'title':'جزئیات هر طبقه',
            'type': 'repeater',
            'fields' : {
            'floor-meterage' : {
                'title':'متراژ طبقه',
                'type': 'number',
            },

            'floor-rooms' : {
                'title':'تعداد اتاق طبقه',
                'type': 'number',
            },
            }
        },


        'light-direction' : {
            'title':'جهت نورگیری',
            'type': 'select',
            'options' : 'light-direction',

            
        },

        'rebuilding' : {
            'title':'وضعیت بازسازی',
            'type': 'radio',
            'options' : 'rebuilding',

        },
        
        'parking' : {
            'title':'پارکینگ',
            'type': 'radio',
            'options' : 'have',
        },

        'parking-status' : {
            'title':'پارکینگ',
            'type': 'radio',
            'options' : 'have',
        },

        'parking-count' : {
            'title':'پارکینگ',
            'type': 'radio',
            'options' : 'have',
        },
        
        'warehouse' : {
            'title':'انباری',
            'type': 'radio',
            'options' : 'have',
        },

        'warehouse-meterage' : {
            'title':'متراژ انباری',
            'type': 'radio',
            'options' : 'have',
        },

        'private-yard' : {
            'title':'حیاط اختصاصی',
            'type': 'radio',
            'options' : 'have',
        },

        'private-yard-meterage' : {
            'title':'متراژ حیاط اختصاصی',
            'type': 'radio',
            'options' : 'have',
        },

        'elevator' : {
            'title':'آسانسور',
            'type': 'radio',
            'options' : 'have',
        },

        'balcony' : {
            'title':'بالکن',
            'type': 'radio',
            'options' : 'have',
        },

        'balcony-meterage' : {
            'title':'متراژ بالکن',
            'type': 'radio',
            'options' : 'have',
        },

        'trass' : {
            'title':'بهار خواب',
            'type': 'radio',
            'options' : 'have',
        },

        'trass-meterage' : {
            'title':'متراژ بهار خواب',
            'type': 'radio',
            'options' : 'have',
        },

        'production-license' : {
            'title':'پروانه ساخت',
            'type': 'radio',
            'options' : 'have',
        },

        'other-features' : {
            'title':'سایر امکانات',
            'type': 'checkbox',
            'options' : 'other-features',
        },

        'branch' : {
            'title':'انشعابات',
            'type': 'branch',
            'options' : 'branch',
        },
        
        'other-features-repeater' : {
            'title':'سایر امکانات',
            'type': 'repeater',
            'fields' : {
            'other-feature-name' : {
                'title':'نام',
                'type': 'text',
            }
            },
            
        },

        'floor-material' : {
            'title':'جنس کف',
            'type': 'group',
            'fields' : {
            
        },

        'other-floor-material' : {
                'title':'',
                'type': 'text',
        },

        'ceiling' : {
            'title':'جنس سقف',
            'type': 'group',
            'fields' : {

            'ceiling' : {
                'title':'جنس سقف',
                'type': 'checkbox',
                'options' : 'ceiling',

            },
            
            'other-ceiling' : {
                'title':'توضیحات',
                'type': 'text',
            },

            }
        },


        'walls' : {
            'title':'جنس دیوار',
            'type': 'group',
            'fields' : {

            'walls' : {
                'title':'جنس دیوار',
                'type': 'checkbox',
                'options' : 'walls',

            },
            
            'other-walls' : {
                'title':'توضیحات',
                'type': 'text',
            },
            },
        },


        'cabinets-material' : {
            'title':'جنس کابینت',
            'type': 'group',
            'fields' : {

            'cabinets-material' : {
                'title':'جنس کابینت',
                'type': 'checkbox',
                'options' : 'cabinets-material',

            },
            
            'other-cabinets-material' : {
                'title':'توضیحات',
                'type': 'text',
            },
            },
        },


        'warming-system' : {
            'title':'سیستم گرمایشی',
            'type': 'group',
            'fields' : {

            'warming-system' : {
                'title':'سیستم گرمایشی',
                'type': 'checkbox',
                'options' : 'warming-system',

            },
            
            'other-warming-system' : {
                'title':'توضیحات',
                'type': 'text',
            },
            },
        },


        'cooling-system' : {
            'title':'سیستم سرمایشی',
            'type': 'group',
            'fields' : {

            'cooling-system' : {
                'title':'سیستم سرمایشی',
                'type': 'checkbox',
                'options' : 'cooling-system',
            },
            
            'other-cooling-system' : {
                'title':'توضیحات',
                'type': 'text',
            },
            },
        },

        'kitchen' : {
            'title':'آشپزخانه',
            'type': 'group',
            'fields' : {

            'kitchen' : {
                'title':'آشپزخانه',
                'type': 'checkbox',
                'options' : 'kitchen',
            },
            
            'other-kitchen-stuff' : {
                'title':'توضیحات',
                'type': 'text',
            },
            },
        },


        'bathroom' : {
            'title':'حمام',
            'type': 'group',
            'fields' : {

            'bathroom' : {
                'title':'حمام',
                'type': 'checkbox',
                'options' : 'bathroom',
            },
            
            'other-bathroom' : {
                'title':'توضیحات',
                'type': 'text',
            },
            },
        },

        'wc' : {
            'title':'سرویس بهداشتی',
            'type': 'group',
            'fields' : {

            'wc' : {
                'title':'سرویس بهداشتی',
                'type': 'checkbox',
                'options' : 'wc',
            },
            
            'other-wc' : {
                'title':'توضیحات',
                'type': 'text',
            },
            },
        },

        'door' : {
            'title':'درب',
            'type': 'group',
            'fields' : {

            'door' : {
                'title':'درب',
                'type': 'checkbox',
                'options' : 'door',
            },
            
            'other-door' : {
                'title':'توضیحات',
                'type': 'text',
            },
            },
        },

        'window' : {
            'title':'پنجره',
            'type': 'group',
            'fields' : {

            'window' : {
                'title':'پنجره',
                'type': 'checkbox',
                'options' : 'window',
                
            },
            
            'other-window' : {
                'title':'توضیحات',
                'type': 'text',
            },
            },
        },

        

        'supplementary_description' : {
            'title':'توضیحات تکمیلی',
            'type': 'textarea',
        },

        'gallery' : {
            'title':'گالری',
            'type': 'textarea',
        },

        }


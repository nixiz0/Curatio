from django.urls import include, path

from .views import panel, register, profile, import_csv
from .functions.lines_columns import *
from .functions.order import *
from .functions.miss_val import *
from .functions.transfo_var import *

# panel/
urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', register, name="register"),
    path('profile/', profile, name="user-profile"),
    path('', panel, name="panel"),
    
    path('upload_csv/', import_csv, name="upload_csv"),
    
    path('delete_column/', del_column, name='del_column'),
    path('del_row/', del_row, name='del_row'),
    path('add_column/', add_column, name='add_column'),
    path('add_row/', add_row, name='add_row'),
    path('modify_column/', modify_column, name='modify_column'),
    path('modify_row/', modify_row, name='modify_row'),
    path('order_by/', order_by, name='order_by'),
    path('reversed_order/', reversed_order, name='reversed_order'),
    path('interval/', interval, name='interval'),
    
    path('miss_val_mean/', miss_val_mean, name='miss_val_mean'),
    path('miss_val_median/', miss_val_median, name='miss_val_median'),
    path('miss_val_std/', miss_val_std, name='miss_val_std'),
    path('miss_val_del/', miss_val_del, name='miss_val_del'),
    path('miss_val_define/', miss_val_define, name='miss_val_define'),
    path('miss_val_mode/', miss_val_mode, name='miss_val_mode'),
    
    path('transfo_var_onehot/', transfo_var_onehot, name='transfo_var_onehot'),
    path('transfo_var_label/', transfo_var_label, name='transfo_var_label'),
    path('transfo_var_ordinal/', transfo_var_ordinal, name='transfo_var_ordinal'),
    path('merge_columns/', merge_columns, name='merge_columns'),
]
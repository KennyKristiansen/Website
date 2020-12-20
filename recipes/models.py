from django import forms
from django.db import models
import django_tables2 as tables

# Create your models here.


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_flag = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Ingredient(models.Model):
    common_key_ingredient = models.ForeignKey('Recipe', on_delete=models.DO_NOTHING)
    ingredient = models.TextField(blank=True, null=False)
    amount = models.IntegerField(blank=True, null=True)
    unit = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ingredient'


class Recipe(models.Model):
    common_key_recipe = models.IntegerField(primary_key=True, blank=False, null=False)
    name = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    calories = models.IntegerField(blank=True, null=True)
    protein = models.IntegerField(blank=True, null=True)
    carbs = models.IntegerField(blank=True, null=True)
    fat = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recipe'


class Steps(models.Model):
    recipe = models.ForeignKey(Recipe, models.DO_NOTHING, blank=True, null=True)
    recipe_step = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'steps'


class RecipeTable(tables.Table):
    class Meta:
        model = Recipe
        template_name = "django_tables2/bootstrap4.html"
        fields = ('name', 'calories', 'protein', 'carbs', 'fat', 'description')


class Nutrient(models.Model):
    index = models.IntegerField(blank=True, null=True)
    id = models.IntegerField(db_column='id', blank=True, primary_key=True)  # Field name made lowercase.
    gruppe = models.TextField(blank=True, null=True)
    navn = models.TextField(db_column='Navn', blank=True, null=True)  # Field name made lowercase.
    svind = models.IntegerField(db_column='Svind', blank=True, null=True)  # Field name made lowercase.
    energi_kj = models.IntegerField(db_column='Energi-kJ', blank=True, null=True)  # Field name made lowercase. Field
    # renamed to remove unsuitable characters.
    energi_kcal = models.IntegerField(db_column='Energi-kcal', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nitrogen_til_protein_faktor = models.FloatField(db_column='Nitrogen-til-protein-faktor', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nitrogen_total = models.FloatField(db_column='Nitrogen-total', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    protein_videnskabelig = models.FloatField(db_column='Protein-videnskabelig', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    protein_deklaration = models.FloatField(db_column='Protein-deklaration', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    kulhydrat_difference_field = models.FloatField(db_column='Kulhydrat-difference-', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    kulhydrat_tilgængelig = models.FloatField(db_column='Kulhydrat-tilgængelig', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    kulhydrat_deklaration = models.FloatField(db_column='Kulhydrat-deklaration', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tilsat_sukker = models.FloatField(db_column='Tilsat-sukker', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    kostfibre = models.FloatField(db_column='Kostfibre', blank=True, null=True)  # Field name made lowercase.
    fedt_total = models.FloatField(db_column='Fedt-total', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fcf = models.FloatField(db_column='FCF', blank=True, null=True)  # Field name made lowercase.
    alkohol = models.FloatField(db_column='Alkohol', blank=True, null=True)  # Field name made lowercase.
    aske = models.FloatField(db_column='Aske', blank=True, null=True)  # Field name made lowercase.
    tørstof = models.FloatField(db_column='Tørstof', blank=True, null=True)  # Field name made lowercase.
    vand = models.FloatField(db_column='Vand', blank=True, null=True)  # Field name made lowercase.
    a_vitamin = models.FloatField(db_column='A-vitamin', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    retinol = models.FloatField(db_column='Retinol', blank=True, null=True)  # Field name made lowercase.
    beta_caroten = models.FloatField(db_column='beta-caroten', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    d_vitamin = models.FloatField(db_column='D-vitamin', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    d3_vitamin = models.FloatField(db_column='D3-vitamin', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    d2_ergocalciferol = models.FloatField(db_column='D2-ergocalciferol', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    e_vitamin = models.FloatField(db_column='E-vitamin', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    alfa_tokoferol = models.FloatField(db_column='alfa-tokoferol', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    gamma_tokoferol = models.FloatField(db_column='gamma-tokoferol', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    delta_tokoferol = models.FloatField(db_column='delta-tokoferol', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    alfa_tokotrienol = models.FloatField(db_column='alfa-tokotrienol', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    k1_vitamin = models.FloatField(db_column='K1-vitamin', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    b1_vitamin = models.FloatField(db_column='B1-vitamin', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thiamin = models.FloatField(blank=True, null=True)
    b2_vitamin_riboflavin = models.FloatField(db_column='B2-vitamin-riboflavin', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    niacinækv0alent = models.FloatField(db_column='Niacinækv0alent', blank=True, null=True)  # Field name made lowercase.
    niacin = models.FloatField(db_column='Niacin', blank=True, null=True)  # Field name made lowercase.
    b6_vitamin = models.FloatField(db_column='B6-vitamin', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pantothensyre = models.FloatField(db_column='Pantothensyre', blank=True, null=True)  # Field name made lowercase.
    biotin = models.FloatField(db_column='Biotin', blank=True, null=True)  # Field name made lowercase.
    folat = models.FloatField(db_column='Folat', blank=True, null=True)  # Field name made lowercase.
    frit_folat = models.FloatField(db_column='Frit-folat', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    b12_vitamin = models.FloatField(db_column='B12-vitamin', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    c_vitamin = models.FloatField(db_column='C-vitamin', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    l_ascorbinsyre = models.FloatField(db_column='L-ascorbinsyre', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    l_dehydroascorbinsyre = models.FloatField(db_column='L-dehydroascorbinsyre', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    svovl_s = models.IntegerField(db_column='Svovl-S', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    chlorid_cl = models.FloatField(db_column='Chlorid-Cl', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    natrium_na = models.FloatField(db_column='Natrium-Na', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    kalium_k = models.FloatField(db_column='Kalium-K', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    calcium_ca = models.FloatField(db_column='Calcium-Ca', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    magnesium_mg = models.FloatField(db_column='Magnesium-Mg', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fosfor_p = models.FloatField(db_column='Fosfor-P', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    jern_fe = models.FloatField(db_column='Jern-Fe', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    kobber_cu = models.FloatField(db_column='Kobber-Cu', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    zink_zn = models.FloatField(db_column='Zink-Zn', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    jod_i = models.FloatField(db_column='Jod-I', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mangan_mn = models.FloatField(db_column='Mangan-Mn', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    chrom_cr = models.FloatField(db_column='Chrom-Cr', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    selen_se = models.FloatField(db_column='Selen-Se', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    molybdæn_mo = models.FloatField(db_column='Molybdæn-Mo', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cobolt_co = models.FloatField(db_column='Cobolt-Co', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nikkel_ni = models.FloatField(db_column='Nikkel-Ni', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fluor_f = models.FloatField(db_column='Fluor-F', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    silicium_si = models.FloatField(db_column='Silicium-Si', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    rubidium_rb = models.IntegerField(db_column='Rubidium-Rb', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    aluminium_al = models.FloatField(db_column='Aluminium-Al', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    bor_b = models.IntegerField(db_column='Bor-B', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    brom_br = models.IntegerField(db_column='Brom-Br', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    kviksølv_hg = models.FloatField(db_column='Kviksølv-Hg', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    arsen_as = models.FloatField(db_column='Arsen-As', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    arsen_uorganisk = models.FloatField(db_column='Arsen-uorganisk', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cadmium_cd = models.FloatField(db_column='Cadmium-Cd', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    bly_pb = models.FloatField(db_column='Bly-Pb', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tin_sn = models.FloatField(db_column='Tin-Sn', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    l_mælkesyre = models.FloatField(db_column='L-mælkesyre', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    d_mælkesyre = models.FloatField(db_column='D-mælkesyre', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mælkesyre_total = models.FloatField(db_column='Mælkesyre-total', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    citronsyre = models.FloatField(db_column='Citronsyre', blank=True, null=True)  # Field name made lowercase.
    oxalsyre = models.FloatField(db_column='Oxalsyre', blank=True, null=True)  # Field name made lowercase.
    æblesyre = models.FloatField(db_column='Æblesyre', blank=True, null=True)  # Field name made lowercase.
    benzoesyre = models.FloatField(db_column='Benzoesyre', blank=True, null=True)  # Field name made lowercase.
    organiske_syrer_tot_field = models.FloatField(db_column='Organiske-syrer-tot.', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    histamin = models.FloatField(db_column='Histamin', blank=True, null=True)  # Field name made lowercase.
    tyramin = models.FloatField(db_column='Tyramin', blank=True, null=True)  # Field name made lowercase.
    phenylethylamin = models.FloatField(db_column='Phenylethylamin', blank=True, null=True)  # Field name made lowercase.
    putrescin = models.FloatField(db_column='Putrescin', blank=True, null=True)  # Field name made lowercase.
    cadaverin = models.FloatField(db_column='Cadaverin', blank=True, null=True)  # Field name made lowercase.
    spermin = models.FloatField(db_column='Spermin', blank=True, null=True)  # Field name made lowercase.
    spermidin = models.FloatField(db_column='Spermidin', blank=True, null=True)  # Field name made lowercase.
    serotonin = models.FloatField(db_column='Serotonin', blank=True, null=True)  # Field name made lowercase.
    fruktose = models.FloatField(db_column='Fruktose', blank=True, null=True)  # Field name made lowercase.
    galaktose = models.FloatField(db_column='Galaktose', blank=True, null=True)  # Field name made lowercase.
    glukose = models.FloatField(db_column='Glukose', blank=True, null=True)  # Field name made lowercase.
    monosaccharider_total = models.FloatField(db_column='Monosaccharider-total', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    laktose = models.FloatField(db_column='Laktose', blank=True, null=True)  # Field name made lowercase.
    maltose = models.FloatField(db_column='Maltose', blank=True, null=True)  # Field name made lowercase.
    sakkarose = models.FloatField(db_column='Sakkarose', blank=True, null=True)  # Field name made lowercase.
    disaccharider_total = models.FloatField(db_column='Disaccharider-total', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    raffinose = models.FloatField(db_column='Raffinose', blank=True, null=True)  # Field name made lowercase.
    andre_sukkerarter = models.FloatField(db_column='Andre-sukkerarter', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sukkerarter_ialt = models.FloatField(db_column='Sukkerarter-ialt', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sorbitol = models.FloatField(db_column='Sorbitol', blank=True, null=True)  # Field name made lowercase.
    inositol = models.FloatField(db_column='Inositol', blank=True, null=True)  # Field name made lowercase.
    maltitol = models.FloatField(db_column='Maltitol', blank=True, null=True)  # Field name made lowercase.
    sukkeralkoholer_total = models.FloatField(db_column='Sukkeralkoholer-total', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    idf = models.FloatField(db_column='IDF', blank=True, null=True)  # Field name made lowercase.
    sdfp = models.FloatField(db_column='SDFP', blank=True, null=True)  # Field name made lowercase.
    sdfs = models.FloatField(db_column='SDFS', blank=True, null=True)  # Field name made lowercase.
    hexose = models.FloatField(db_column='Hexose', blank=True, null=True)  # Field name made lowercase.
    pentose = models.FloatField(db_column='Pentose', blank=True, null=True)  # Field name made lowercase.
    uronic_acid = models.FloatField(db_column='Uronic-Acid', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cellulose = models.FloatField(db_column='Cellulose', blank=True, null=True)  # Field name made lowercase.
    lignin = models.FloatField(db_column='Lignin', blank=True, null=True)  # Field name made lowercase.
    crude_fibre = models.FloatField(db_column='Crude-fibre', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    andre_mættede_fedtsyrer = models.FloatField(db_column='Andre-mættede-fedtsyrer', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    andre_monoumættede_fedtsyrer = models.FloatField(db_column='Andre-monoumættede-fedtsyrer', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    andre_polyumættede = models.FloatField(db_column='Andre-polyumættede', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    andre_fedtsyrer = models.FloatField(db_column='Andre-fedtsyrer', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sum_mættede = models.FloatField(db_column='Sum-mættede', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sum_monoumættede = models.FloatField(db_column='Sum-monoumættede', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sum_polyumættede = models.FloatField(db_column='Sum-polyumættede', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    transfedtsyrer_total = models.FloatField(db_column='Transfedtsyrer-total', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fedtsyrer_total = models.FloatField(db_column='Fedtsyrer-total', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'nutrient'


class NutrientTable(tables.Table):
    class Meta:
        model = Nutrient
        template_name = "django_tables2/bootstrap4.html"
        fields = ('id', 'navn', 'energi_kj', 'protein_videnskabelig', 'kulhydrat_tilgængelig', 'fedt_total', 'svind')

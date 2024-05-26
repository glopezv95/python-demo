# FIELDS ----------

PEOPLE_DICT = {
    'name': 'VARCHAR(50)',
    'lastname': 'VARCHAR(50)',
    'gender': 'VARCHAR(6)',
    'age': 'INT',
    'birth_province': 'VARCHAR(50)',
    'studies': 'VARCHAR(9)',
    'department': 'VARCHAR(100)',
    'partner': 'BOOL',
    'salary': 'NUMERIC(9,2)',
    'years_in_company': 'INT',
    'remote_days': 'INT',
    'input_date': 'TIMESTAMPTZ'
}

CCAA_DICT = {
    'name': 'VARCHAR(50)',
    'code': 'VARCHAR(2)'
}

PROVINCE_DICT = {
    'ccaa_code': 'VARCHAR(50)',
    'name': 'VARCHAR(50)',
    'code': 'VARCHAR(2)'
}

DEPARTMENTS_DICT = {
    'name': 'VARCHAR(100)',
    'created': 'INT',
    'director': 'VARCHAR(50)',
    'contact_email': 'VARCHAR(50)'
}

PROJECTS_DICT = {
    'name': 'VARCHAR(100)',
    'year': 'INT',
    'department': 'VARCHAR(100) []',
    'budget': 'NUMERIC(9,2)'
}

# MISC ----------

CCAA_JSON = {
    "Andalucía": {
        "provincias": ["Almería", "Cádiz", "Córdoba", "Granada", "Huelva", "Jaén", "Málaga", "Sevilla"],
        "códigos ISO": ["AL", "CA", "CO", "GR", "H", "J", "MA", "SE"],
        "código autonómico": "AN"
    },
    "Aragón": {
        "provincias": ["Huesca", "Teruel", "Zaragoza"],
        "códigos ISO": ["HU", "TE", "Z"],
        "código autonómico": "AR"
    },
    "Asturias": {
        "provincias": ["Asturias"],
        "códigos ISO": ["O"],
        "código autonómico": "AS"
    },
    "Islas Baleares": {
        "provincias": ["Islas Baleares"],
        "códigos ISO": ["PM"],
        "código autonómico": "IB"
    },
    "País Vasco": {
        "provincias": ["Álava", "Vizcaya", "Guipúzcoa"],
        "códigos ISO": ["VI", "BI", "SS"],
        "código autonómico": "PV"
    },
    "Islas Canarias": {
        "provincias": ["Las Palmas", "Santa Cruz de Tenerife"],
        "códigos ISO": ["GC", "TF"],
        "código autonómico": "CN"
    },
    "Cantabria": {
        "provincias": ["Cantabria"],
        "códigos ISO": ["S"],
        "código autonómico": "CB"
    },
    "Castilla y León": {
        "provincias": ["Ávila", "Burgos", "León", "Palencia", "Salamanca", "Segovia", "Soria", "Valladolid", "Zamora"],
        "códigos ISO": ["AV", "BU", "LE", "P", "SA", "SG", "SO", "VA", "ZA"],
        "código autonómico": "CL"
    },
    "Castilla-La Mancha": {
        "provincias": ["Albacete", "Ciudad Real", "Cuenca", "Guadalajara", "Toledo"],
        "códigos ISO": ["AB", "CR", "CU", "GU", "TO"],
        "código autonómico": "CM"
    },
    "Cataluña": {
        "provincias": ["Barcelona", "Girona", "Lleida", "Tarragona"],
        "códigos ISO": ["B", "GI", "L", "T"],
        "código autonómico": "CT"
    },
    "Extremadura": {
        "provincias": ["Badajoz", "Cáceres"],
        "códigos ISO": ["BA", "CC"],
        "código autonómico": "EX"
    },
    "Galicia": {
        "provincias": ["A Coruña", "Lugo", "Ourense", "Pontevedra"],
        "códigos ISO": ["C", "LU", "OR", "PO"],
        "código autonómico": "GA"
    },
    "Madrid": {
        "provincias": ["Madrid"],
        "códigos ISO": ["M"],
        "código autonómico": "MD"
    },
    "Murcia": {
        "provincias": ["Murcia"],
        "códigos ISO": ["MU"],
        "código autonómico": "MC"
    },
    "Navarra": {
        "provincias": ["Navarra"],
        "códigos ISO": ["NA"],
        "código autonómico": "NC"
    },
    "La Rioja": {
        "provincias": ["La Rioja"],
        "códigos ISO": ["LO"],
        "código autonómico": "RI"
    },
    "Comunidad Valenciana": {
        "provincias": ["Alicante", "Castellón", "Valencia"],
        "códigos ISO": ["A", "CS", "V"],
        "código autonómico": "VC"
    }
}

PROVINCES = [
    "Álava", "Albacete", "Alicante", "Almería", "Asturias", "Ávila", "Badajoz", "Baleares",
    "Barcelona", "Burgos", "Cáceres", "Cádiz", "Cantabria", "Castellón", "Ceuta", "Ciudad Real",
    "Córdoba", "Cuenca", "Gerona", "Granada", "Guadalajara", "Guipúzcoa", "Huelva", "Huesca",
    "Jaén", "La Coruña", "La Rioja", "Las Palmas", "León", "Lérida", "Lugo", "Madrid", "Málaga",
    "Melilla", "Murcia", "Navarra", "Orense", "Palencia", "Pontevedra", "Salamanca", "Segovia",
    "Sevilla", "Soria", "Tarragona", "Santa Cruz de Tenerife", "Teruel", "Toledo", "Valencia",
    "Valladolid", "Vizcaya", "Zamora", "Zaragoza"
]

GENDER = ['female', 'male']
STUDIES = ['primary', 'secondary', 'tertiary']
PARTNER = [True, False]

DEPARTMENTS = [
    "Recursos Humanos",
    "Finanzas",
    "Contabilidad",
    "Ventas",
    "Marketing",
    "Operaciones",
    "Logística",
    "Tecnología de la Información (TI)",
    "Investigación y Desarrollo (I+D)",
    "Servicio al Cliente",
    "Compras",
    "Producción",
    "Legal",
    "Calidad",
    "Comunicación Corporativa",
    "Desarrollo de Negocios",
    "Relaciones Públicas",
    "Gestión de Proyectos",
    "Formación y Desarrollo",
    "Administración",
    "Seguridad y Salud Ocupacional",
    "Medio Ambiente",
    "Innovación",
    "Análisis de Datos",
    "Estrategia Corporativa"
]

PROJECTS = [
    "Transformación Digital",
    "Optimización de Procesos",
    "Expansión de Mercado",
    "Mejora de la Experiencia del Cliente",
    "Automatización de la Producción",
    "Implementación de ERP",
    "Desarrollo de Nuevos Productos",
    "Sostenibilidad y Medio Ambiente",
    "Capacitación y Desarrollo de Talento",
    "Eficiencia Energética",
    "Modernización de Infraestructura TI",
    "Estrategia de Marketing Digital",
    "Programa de Cumplimiento Legal",
    "Innovación en la Cadena de Suministro",
    "Análisis de Big Data",
    "Programa de Diversidad e Inclusión",
    "Seguridad de la Información",
    "Integración Post-Adquisición",
    "Reducción de Costos",
    "Fortalecimiento de la Cultura Organizacional",
    "Desarrollo de Software Personalizado",
    "Fidelización de Clientes",
    "Implementación de CRM",
    "Optimización de Inventarios",
    "Proyecto de Inteligencia Artificial",
    "Mejora de Procesos Financieros",
    "Desarrollo de Plataforma E-commerce",
    "Estrategia de Publicidad Online",
    "Proyecto de Movilidad Sostenible",
    "Gestión del Cambio Organizacional",
    "Desarrollo de Red de Distribución",
    "Mejora de Procesos Logísticos",
    "Certificación de Calidad",
    "Programa de Salud y Bienestar",
    "Auditoría Interna de Procesos",
    "Automatización del Servicio al Cliente",
    "Desarrollo de Aplicaciones Móviles",
    "Optimización de la Fuerza de Ventas",
    "Reestructuración Corporativa",
    "Plan de Continuidad del Negocio",
    "Proyecto de Blockchain",
    "Implementación de IoT",
    "Renovación de Marca",
    "Proyecto de Ciberseguridad",
    "Automatización de Recursos Humanos",
    "Optimización del Ciclo de Vida del Producto",
    "Implementación de Sistemas de Gestión Ambiental",
    "Desarrollo de Estrategia Omnicanal",
    "Expansión Internacional",
    "Mejora de la Retención de Empleados"
]
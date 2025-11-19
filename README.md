# Calculadora de Sistema Solar

Aplicación web desarrollada con React y Vite para calcular los parámetros de un sistema de energía solar fotovoltaica.

## Características

La aplicación calcula:
- **Potencia del sistema solar** en KW
- **Número de paneles** necesarios (paneles de 550W)
- **Ahorro mensual** en COP
- **Costo de instalación** del sistema
- **Años de retorno de inversión**
- **Área requerida** para la instalación

## Instalación

1. Instalar las dependencias:
```bash
npm install
```

2. Ejecutar en modo desarrollo:
```bash
npm run dev
```

3. Construir para producción:
```bash
npm run build
```

## Parámetros del Sistema

- Potencia por panel: 550 W
- Horas de sol efectivas: 5 horas/día (promedio en Colombia)
- Costo KWh: $926 COP
- Costo instalación: $2,100,000 COP por panel
- Factor de seguridad: 25%
- Área por panel: 2.2 m²

## Tecnologías

- React 18
- Vite
- CSS3


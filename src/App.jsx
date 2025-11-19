import React, { useState } from 'react'
import './App.css'

function App() {
  const [kwhMensual, setKwhMensual] = useState('')
  const [resultados, setResultados] = useState(null)

  // Constantes del sistema
  const POTENCIA_PANEL_W = 550 // Potencia de cada panel en Watts
  const COSTO_KWH_COP = 926 // Costo del KWh en COP
  const COSTO_INSTALACION_POR_PANEL_COP = 2100000 // Costo de instalación por panel en COP
  const HORAS_SOL_DIARIAS = 5 // Horas efectivas de sol por día (promedio en Colombia)
  const DIAS_MES = 30 // Días promedio por mes
  const AREA_POR_PANEL_M2 = 2.2 // Área aproximada por panel en m² (paneles de 550W)
  const FACTOR_SEGURIDAD = 1.25 // Factor de seguridad para dimensionamiento

  const calcularSistemaSolar = () => {
    const kwh = parseFloat(kwhMensual)
    
    if (isNaN(kwh) || kwh <= 0) {
      alert('Por favor ingrese un valor válido de KWh mensual')
      return
    }

    // 1. Calcular potencia del sistema en KW
    // Potencia necesaria = (KWh mensual / (horas sol * días mes)) * factor de seguridad
    const potenciaKW = (kwh / (HORAS_SOL_DIARIAS * DIAS_MES)) * FACTOR_SEGURIDAD

    // 2. Calcular número de paneles
    const numeroPaneles = Math.ceil((potenciaKW * 1000) / POTENCIA_PANEL_W)

    // 3. Calcular ahorro mensual
    const ahorroMensual = kwh * COSTO_KWH_COP

    // 4. Calcular costo de instalación
    const costoInstalacion = numeroPaneles * COSTO_INSTALACION_POR_PANEL_COP

    // 5. Calcular años de retorno de inversión
    const ahorroAnual = ahorroMensual * 12
    const anosRetorno = costoInstalacion / ahorroAnual

    // 6. Calcular área a utilizar
    const areaTotal = numeroPaneles * AREA_POR_PANEL_M2

    setResultados({
      potenciaKW: potenciaKW.toFixed(2),
      numeroPaneles,
      ahorroMensual: ahorroMensual.toLocaleString('es-CO'),
      costoInstalacion: costoInstalacion.toLocaleString('es-CO'),
      anosRetorno: anosRetorno.toFixed(2),
      areaTotal: areaTotal.toFixed(2)
    })
  }

  const formatearNumero = (numero) => {
    return numero.toLocaleString('es-CO', { minimumFractionDigits: 0, maximumFractionDigits: 0 })
  }

  return (
    <div className="app">
      <div className="container">
        <header className="header">
          <h1>☀️ Calculadora de Sistema Solar</h1>
          <p className="subtitle">Calcula los parámetros de tu sistema de energía solar</p>
        </header>

        <div className="input-section">
          <label htmlFor="kwh-input" className="label">
            Gasto Energético Mensual (KWh)
          </label>
          <input
            id="kwh-input"
            type="number"
            className="input"
            placeholder="Ej: 500"
            value={kwhMensual}
            onChange={(e) => setKwhMensual(e.target.value)}
            min="0"
            step="0.1"
          />
          <button 
            className="button"
            onClick={calcularSistemaSolar}
          >
            Calcular
          </button>
        </div>

        {resultados && (
          <div className="results-section">
            <h2 className="results-title">Resultados del Sistema</h2>
            
            <div className="result-card">
              <div className="result-icon">⚡</div>
              <div className="result-content">
                <div className="result-label">Potencia del Sistema</div>
                <div className="result-value">{resultados.potenciaKW} KW</div>
              </div>
            </div>

            <div className="result-card">
              <div className="result-icon">🔋</div>
              <div className="result-content">
                <div className="result-label">Número de Paneles (550W)</div>
                <div className="result-value">{resultados.numeroPaneles} paneles</div>
              </div>
            </div>

            <div className="result-card">
              <div className="result-icon">💰</div>
              <div className="result-content">
                <div className="result-label">Ahorro Mensual</div>
                <div className="result-value">${resultados.ahorroMensual} COP</div>
              </div>
            </div>

            <div className="result-card">
              <div className="result-icon">💵</div>
              <div className="result-content">
                <div className="result-label">Costo de Instalación</div>
                <div className="result-value">${resultados.costoInstalacion} COP</div>
              </div>
            </div>

            <div className="result-card">
              <div className="result-icon">📅</div>
              <div className="result-content">
                <div className="result-label">Retorno de Inversión</div>
                <div className="result-value">{resultados.anosRetorno} años</div>
              </div>
            </div>

            <div className="result-card">
              <div className="result-icon">📐</div>
              <div className="result-content">
                <div className="result-label">Área Requerida</div>
                <div className="result-value">{resultados.areaTotal} m²</div>
              </div>
            </div>
          </div>
        )}

        <div className="info-section">
          <h3 className="info-title">Información del Cálculo</h3>
          <ul className="info-list">
            <li>Potencia por panel: 550 W</li>
            <li>Horas de sol efectivas: 5 horas/día</li>
            <li>Costo KWh: $926 COP</li>
            <li>Costo instalación: $2,100,000 COP por panel</li>
            <li>Factor de seguridad: 25%</li>
          </ul>
        </div>
      </div>
    </div>
  )
}

export default App


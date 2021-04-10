.. _physical_properties_index:

Propriedades Físicas
====================

.. purpose::
    
    Para gerar um recurso que tem uma compilação de valores para físicos
    propriedades em função do tipo de rocha, composição mineral e saturação
    fluidos. Histórico sobre como as medições de laboratório são feitas e as
    conexão com as relações constitutivas são apresentadas. Cada seção
    começará com exemplos de onde a propriedade física particular tem
    sido diagnosticada.
    
Uma propriedade física quantifica como uma rocha responde a um determinado fenômeno físico, como ondas sonoras por exemplo. Em geofísica eletromagnética, as propriedades físicas relevantes são:

- :ref:`electrical_conductivity_index`: :math:`\sigma` (ou sua recíproca, resistividade, :math:`\rho`)
- :ref:`magnetic_permeability_index`, :math:`\mu`
- :ref:`dielectric_permittivity_index`, :math:`\varepsilon`

As propriedades físicas eletromagnéticas são definidas usando um conjunto de relações constitutivas. Cada relação constitutiva caracteriza o fluxo resultante devido a um campo de força causal. Na maioria dos casos, as medições de laboratório são realizadas no domínio da frequência, mas podem ser realizadas no domínio do tempo. Se as propriedades físicas não forem dispersivas, a relação entre o campo e o fluxo correspondente é independente da frequência. Assim, as relações constitutivas são dadas por:

- :math:`\mathbf{J}(\omega)= \sigma \mathbf{E}(\omega)`  (Lei de Ohm)
- :math:`\mathbf{B}(\omega)= \mu \mathbf{H}(\omega)`
- :math:`\mathbf{D}(\omega)= \varepsilon \mathbf{E}(\omega)`

Ao tomar a transformada inversa de Fourier, as suas propriedades correspondentes no domínio do tempo são dados por:

- :math:`\mathbf{j}(t)= \sigma \mathbf{e}(t)`  (Lei de Ohm)
- :math:`\mathbf{b}(t)= \mu \mathbf{h}(t)`
- :math:`\mathbf{d}(t)= \varepsilon \mathbf{e}(t)`

**Dispersão**

A dispersão implica que uma determinada propriedade física depende da frequência. A condutividade elétrica, a permeabilidade magnética e a permissividade dielétrica exibem propriedades dispersivas sob várias condições. Para propriedades físicas dispersivas, as relações constitutivas são dadas por:

- :math:`\mathbf{J}(\omega)= \sigma (\omega) \mathbf{E}(\omega)`  (Lei de Ohm)
- :math:`\mathbf{B}(\omega)= \mu (\omega) \mathbf{H}(\omega)`
- :math:`\mathbf{D}(\omega)= \varepsilon (\omega) \mathbf{E}(\omega)`

Mais uma vez, o equivalente no domínio do tempo para as relações constitutivas pode ser obtido tomando a transformada inversa de Fourier. Se as propriedades físicas são dispersivas, a relação entre cada campo e seu fluxo correspondente torna-se uma convolução:

- :math:`\mathbf{j}(t)=\sigma(t) \ast \mathbf{e}(t)`
- :math:`\mathbf{b}(t)=\mu(t) \ast \mathbf{h}(t)`
- :math:`\mathbf{d}(t)=\varepsilon(t) \ast \mathbf{e}(t)`

**Anisotropia**

Anisotropia significa que a resposta física de uma rocha a um campo aplicado não é a mesma em todas as direções. Neste caso, cada campo e seu fluxo correspondente são relacionados por um tensor :math:`3\times 3`:

- :math:`\mathbf{J}= \Sigma \mathbf{E}`
- :math:`\mathbf{B}= \Gamma \mathbf{H}`
- :math:`\mathbf{D}= \Upsilon \mathbf{E}`

onde

.. math::
    \Sigma = \begin{bmatrix} \sigma_{xx} & \sigma_{xy} & \sigma_{xz} \\ \sigma_{yx} & \sigma_{yy} & \sigma_{yz} \\ \sigma_{zx} & \sigma_{zy} & \sigma_{zz} \end{bmatrix} , \; \;
    \Gamma = \begin{bmatrix} \mu_{xx} & \mu_{xy} & \mu_{xz} \\ \mu_{yx} & \mu_{yy} & \mu_{yz} \\ \mu_{zx} & \mu_{zy} & \mu_{zz} \end{bmatrix} \; \; \textrm{and} \; \;
    \Upsilon = \begin{bmatrix} \varepsilon_{xx} & \varepsilon_{xy} & \varepsilon_{xz} \\ \varepsilon_{yx} & \varepsilon_{yy} & \varepsilon_{yz} \\ \varepsilon_{zx} & \varepsilon_{zy} & \varepsilon_{zz} \end{bmatrix} , \; \;

As relações constitutivas, junto com as equações de Maxewll, formam um conjunto completo de equações para eletromagnetismo. Nesta seção, apresentamos o material básico sobre as várias propriedades físicas. Para cada propriedade, oferecemos:

- a relação constitutiva, uma descrição física e sua relevância para a geociência eletromagnética
- uma descrição das técnicas comuns de medição de laboratório
- tabelas contendo uma faixa típica de valores
- uma lista de fatores que controlam o valor da propriedade física
- referências

**Contents:**

.. toctree::
    :maxdepth: 1

    electrical_conductivity/index
..    magnetic_permeability/index
..    dielectric_permittivity/index

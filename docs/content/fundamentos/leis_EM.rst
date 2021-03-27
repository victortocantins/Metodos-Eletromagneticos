.. _leis_EM:

Leis do eletromagnetismo
========================

Aqui, as leis básicas que regem o eletromagnetismo são apresentadas. As definições formais são fornecidas junto com as descrições matemáticas apropriadas.

Introdução
----------

.. note::

    Não apresentaremos um tratamento rigoroso sobre as leis do eletromagnetismo, mas apenas o que acahmos mais 
    importante ao entendimento dos meétodos eletromagnéticos. Textos mais dedicado a este assunto são inúmeros e de
    execelente qualidade. Podemos citar como exemplos os livros de :cite:`Jackson`, :cite:`stratton1941` e 
    :cite:`harrington2001time`

Lei de Gauss
------------
Carga elétrica
**************
A carga elétrica fundamental na natureza é a carga do elétron. O fato de que existe uma carga elétrica era conhecido pelos antigos
gregos que sabiam que esfregar um pedaço de âmbar na pele ou tecido causava a atração de partículas como
penas, palha ou fiapos. Elétron é o nome grego para âmbar. Demorou muitos anos antes que fosse compreendido o que realmente
acontecia neste tipo de experimento ou a quantificar a carga elétrica associada ao elétron, mas os efeitos da carga estavam
por toda parte para serem observados. Para que um corpo contenha cargas livres, deve haver uma maneira de remover
elétrons de um corpo e transmiti-las a outro. O corpo do qual os elétrons são removidos torna-se positivamente
carregado (por causa do excesso de prótons), enquanto o outro corpo torna-se carregado negativamente (excesso de elétrons).
Isso é o que aconteceu quando o âmbar foi esfregado com pêlo: Elétrons foram removidos do pêlo e depositados no âmbar.
A ação de esfregar forneceu a energia necessária para que os elétrons fossem removidos. O âmbar, portanto, tornou-se carregado
negativamente e poderia atrair pequenos pedaços de material. Ao mesmo tempo, a pele ficou carregada positivamente. 
Nós sabemos que um raio ocorre quando carga se acumula além de um certo nível. Isso significa que as cargas devem se acumular 
em um volume ou sobre uma superfície. Uma vez que sabemos que a carga elétrica causa forças em sua vizinhança, essa força também 
deve ser proporcional à quantidade de cargas. Antes de quantificarmos os efeitos da carga elétrica, devemos estabelecer algumas preliminares. 
Isso inclui a carga do elétron, a unidade de carga e as definições de cargas pontuais e cargas distribuídas.

A unidade de carga é chamada de **coulomb**. A carga de um elétron é denotada por  :math:`e`, e é igual a :math:`-1.6019 \times 10
^{-19}` C. Ou seja, um coulomb é igual à carga de aproximadamente :math:`6.25\times 10^{18}` elétrons. A carga do elétron é 
considerada para ser a menor unidade de carga e todas as cargas devem ser múltiplos dessa quantidade, embora a carga possa
ser positiva ou negativa. A carga pode ser distribuída no espaço ou pode ser concentrada em um pequeno volume ou um "ponto".

**Carga Pontual.** Uma carga que ocupa um volume no espaço pode ser considerada uma carga pontual para fins de análise se este 
volume é pequeno em comparação com as dimensões circundantes. As cargas de elétrons ou prótons são frequentemente consideradas 
cargas pontuais. Para fins práticos, outras cargas, como a carga de uma esfera ou qualquer outro pequeno volume, são frequentemente 
consideradas serem cargas pontuais, desde que estejamos longe do volume.

Uma densidade de carga define uma carga distribuída sobre um corpo. Existem três tipos de densidades de carga:

**Densidade de carga linear.**  A distribuição de é carga linear, como ao longo de um fio muito fino, é definida como 
carga por unidade comprimento. Uma densidade de carga de 1 C/m significa que um coulomb de carga é distribuído por 
cada metro de comprimento do dispositivo (como um fio). Uma descrição mais exata da densidade de carga da linha é 
dizer que a densidade de carga é a carga :math:`\Delta Q` distribuído ao longo de um comprimento :math:`\Delta Q` 
conforme :math:`\Delta l` se aproxima de zero, como é definido pela Equação :eq:`dlin`

.. math::
    :label: dlin

    \rho_l = \lim_{\Delta l \to 0}\frac{\Delta Q}{\Delta l} \quad \left[\frac{\mathrm{C}}{\mathrm{m}}\right].

**Densidade de carga superficial.** É quando a carga distribuída sobre uma determinada superfície, como a 
superfície de uma esfera ou uma folha de papel. Uma densidade de carga superficial de :math:`1\, \mathrm{C}/\mathrm{m}^2` 
significa que um coulomb de carga é distribuído por cada metro quadrado da superfície. A densidade de carga superficial é 
definida matematicamente pela Equação :eq:`darea`

.. math::
    :label: darea

    \rho_s = \lim_{\Delta s \to 0}\frac{\Delta Q}{\Delta s} \quad \left[\frac{\mathrm{C}}{\mathrm{m}^2}\right].

**Densidade de carga volumétrica.** A carga é distribuída em um volume, como o volume de uma nuvem. 
Uma densidade de carga de volume de :math:`1\, \mathrm{C}/\mathrm{m}^3` significa que um coulomb de carga é distribuído 
sobre um cubo de um metro de volume e dada pela Equação :eq:`dvol`:

.. math::
    :label: dvol

    \rho_v = \lim_{\Delta v \to 0}\frac{\Delta Q}{\Delta v} \quad \left[\frac{\mathrm{C}}{\mathrm{m}^3}\right].

As densidades de carga nas Equações. :eq:`dlin` a :eq:`dvol` podem ser uniformes ou não uniformes nas dimensões 
fornecidas. Uma densidade  uniforme  de carga significa que a carga distribuída por qualquer seção igual de superfície, 
linha ou volume é a mesma; ou seja, é independente das variáveis. Uma densidade de carga não uniforme ocorre quando a carga 
em diferentes seções da distribuição depende da localização. Observe, também, que as densidades de carga fornecidas acima 
como exemplos são eaxgeradas. Normalmente, densidades de carga muito menores são encontradas na realidade.